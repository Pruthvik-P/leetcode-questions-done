type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    const results = await Promise.all([promise1, promise2])
    return results[0] + results[1]
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
