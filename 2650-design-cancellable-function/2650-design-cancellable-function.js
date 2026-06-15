/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    let cancelled = false;

    const cancel = () => {
        cancelled = true;
    };

    const promise = new Promise(async (resolve, reject) => {
        let next;

        try {
            next = generator.next();

            while (!next.done) {
                try {
                    const value = await next.value;

                    if (cancelled) {
                        next = generator.throw("Cancelled");
                    } else {
                        next = generator.next(value);
                    }

                } catch (err) {

                    if (cancelled) {
                        next = generator.throw("Cancelled");
                    } else {
                        next = generator.throw(err);
                    }
                }
            }

            resolve(next.value);

        } catch (err) {
            reject(err);
        }
    });

    return [cancel, promise];
};