class MedianFinder {
private:
    priority_queue<int,vector<int>,less<int> >maxheap ;//大顶堆，但是堆顶是这个堆里面最小的数
    priority_queue<int,vector<int>,greater<int> >minheap ;//小顶堆，但是堆顶存的是这个堆里面最大的数
public:

    // Adds a number into the data structure.
    void addNum(int num) {
        int t,maxlen,minlen;
        maxheap.push(num);
        t=maxheap.top();
        maxheap.pop();
        minheap.push(t);
        maxlen=maxheap.size();
        minlen=minheap.size();
        if(minlen-maxlen>0){
            t=minheap.top();
            minheap.pop();
            maxheap.push(t);
        }
    }

    // Returns the median of current data stream
    double findMedian() {
        int m,n;
        m=maxheap.size();
        n=minheap.size();
        if(m==n){
            return (maxheap.top()+minheap.top())/2.0;
        }
        else{
            if(m>n){
                return maxheap.top();
            }
            else{
                return minheap.top();
            }
        }
    }
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf;
// mf.addNum(1);
// mf.findMedian();
