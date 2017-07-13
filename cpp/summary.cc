// If a method in a base class will be redefined in a derived class, you should make it virtual.
// If the method should not be redefined, you should make it nonvirtual.

// The difference between private and protected comes into play only within classes derived from the base class. 
// Members of a derived class can access protected members of a base class directly, but they can- not directly access private members of the base class.

auto a= 3;

std::function
std::call_once

std::iota

std::tie
std::swap(a, b);
std::forward();

std::memcpy();
std::numeric_limits<size_t>::max();

//std::move is used to indicate that an object t may be "moved from", i.e. allowing the efficient transfer of resources from t to another object.
std::move();
// std::string str = "Hello";
// std::vector<std::string> v;
// v.push_back(str); // str is still "Hello", a deep copy
// v.push_back(std::move(str)); // str is now "", moved here
// Always combined with unique_ptr

std::copy();

std::sort();
std::min();
std::max();
std::equal();
std::complex;
std::tuple<int, int>;
std::find();

std::get<0> lrs;
std::normal_distribution<double>
int32 dim = std::uniform_int_distribution<int32>;
std::uniform_int_distribution<int> random_int(1, 5);
std::bernoulli_distribution random_bool;
std::shuffle();
std::uniform_real_distribution<float> distribution(-1.0f, 1.0f);

std::vector<int>;
std::pair;
std::make_pair;
std::unordered_set<string> a;
std::unordered_map<string, int> a;
std::map
std::array
std::deque<int> a;
std::hash;


std::initializer_list<TF_Operation*>

/* smart pointers */
// added benefit over using raw pointers is automatic memory management of dynamically allocated resources, so that you don't have to make explicit calls to delete.
//Use a unique_ptr when an object claims ownership of a resource. That is, the object is responsible for managing the memory of the resource, deleting it when it's own destructor is called. Also, note that the assignment operator of a unique_ptr only accepts rvalues, which should be provided by std::move semantics.
std::unique_ptr<int> v1 = std::make_unique<int>(3);

//Use a shared_ptr when you heap-allocate a resource that needs to be shared among multiple objects. It maintains a reference count internally and only deletes the resource when the reference count goes to zero.
// std::shared_ptr, return a std::shared_ptr of instance type T
// defined in header <memory> as
// template<class T, class... Args>
// shared_ptr<T> make_shared(Args&&... args);
// recommends this than shtd::shared_ptr<T>(new T(args))
auto sp = std::make_shared<int>(12);
std::shared_ptr<int> spp = std::make_shared<int>(10);

