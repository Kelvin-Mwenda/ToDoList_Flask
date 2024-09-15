const jobs = Array.from({length:100}, () => 19)
console.log(jobs);
const tick = performance.now()
for ( let job of jobs ){
    let count = 0;
    for (let i = 0; i < job; i++){
        console.log(count)
        count++
    }
}

const tock = performance.now()
console.log(`Main thread took ${tock - tick} ms `)