export function processArray(items, process) {
    var todo = items.concat();
    console.log(arguments);
    setTimeout(function() {
        process(todo.shift());
        if(todo.length > 0) {
            setTimeout(arguments.callee, 25);
        }
    }, 25);
}
