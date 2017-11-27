/* The basic idea is to pick each offer, and subtract the needs. And then compute the price without the offer.
Pick whichever is minimum.

Edit : ) much appreciated if someone can shorten the code with Java8 :)
*/

public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
    int result = Integer.MAX_VALUE;
    //apply each offer to the needs, and recurse
    for(int i = 0; i < special.size(); i++) {
        List<Integer> offer = special.get(i);
        boolean invalidOffer = false;
        for(int j = 0; j < needs.size(); j++) { // subtract offer items from needs
            int remain = needs.get(j) - offer.get(j);
            needs.set(j, remain);
            if(!invalidOffer && remain < 0) invalidOffer = true; // if offer has more items than needs
        }
        if(!invalidOffer) { //if valid offer, add offer price and recurse remaining needs
            result = Math.min(result, shoppingOffers(price, special, needs) + offer.get(needs.size()));
        }
        for(int j = 0; j < needs.size(); j++) { // reset the needs
            int remain = needs.get(j) + offer.get(j);
            needs.set(j, remain);
        }
    }
    // choose b/w offer and non offer
    int nonOfferPrice = 0;
    for(int i = 0; i < needs.size(); i++) {
        nonOfferPrice += price.get(i) * needs.get(i);
    }
    return Math.min(result, nonOfferPrice);
}

/*
UPDATE 1 : For the below test case, we get time limit exceeded since it's exponential. TLE due to needs=30+.
I've requested admins to add this testcase.

[2,5]
[[1,0,5],[1,2,10]]
[39,39]
So I made some optimization to reduce the recursive calls, by precomputing the number of times offer can be applied. See UPDATE 3, there's an example that breaks this greedy optimization.
*/

    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        int result = Integer.MAX_VALUE;
        //apply each offer to the needs, and recurse
        for(int i = 0; i < special.size(); i++) {
            List<Integer> offer = special.get(i);
            boolean invalidOffer = false;
            int offerCount = Integer.MAX_VALUE; // number of times offer can be applied
            for(int j = 0; j < needs.size(); j++) { // pre-compute number of times offer can be called
                int remain = needs.get(j) - offer.get(j);
                if(!invalidOffer && remain < 0) invalidOffer = true; // if offer has more items than needs
                if(offer.get(j) > 0)
                offerCount = Math.min(offerCount, needs.get(j)/offer.get(j));
            }
            for(int j = 0; j < needs.size(); j++) { // subtract offer items from needs
                int remain = needs.get(j) - offer.get(j) * offerCount;
                needs.set(j, remain);
            }
            if(!invalidOffer) { //if valid offer, add offer price and recurse remaining needs
                result = Math.min(result, shoppingOffers(price, special, needs) + (offerCount * offer.get(needs.size())));
            }

            for(int j = 0; j < needs.size(); j++) { // reset the needs
                int remain = needs.get(j) + offer.get(j) * offerCount;
                needs.set(j, remain);
            }
        }

        // choose b/w offer and non offer
        int nonOfferPrice = 0;
        for(int i = 0; i < needs.size(); i++) {
            nonOfferPrice += price.get(i) * needs.get(i);
        }
        return Math.min(result, nonOfferPrice);
    }
/*
UPDATE 2: I think OJ is breaking with the below test case. My code handles it though. Expected output is 8000, since it has two items of 1$ each. I've requested to add the test case. Also, another assumption is that result doesn't exceed Integer.MAX_VALUE. @administrators

[1,1]
[[1,1,2],[1,1,3]]
[4000,4000]
UPDATE 3: From @Red_Eden 's thought, I found a test case that breaks my optimization. OJ is missing this test as well. My solution gives answer = 6, but actual is pick one offer just once = 4.

[500]
[[2,1],[3,2],[4,1]]
[9]
*/
