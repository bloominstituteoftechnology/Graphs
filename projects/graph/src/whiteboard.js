/**
 * @param {number[]} A
 * @return {number[]}
 */
const sortArrayByParity = function(A) {
    const even = []
    const odd = []
    for (let i=0; i < A.length; i++){
        if (A[i] % 2 == 0){
            even.push(A[i])
        } else {
            odd.push(A[i])
        }
    }
    return even.concat(odd)
};

/*
O(c)
O(n)
O(n^2)
*/