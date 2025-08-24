// ES6_basic/1-block-scoped.js
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;   // Scoped only inside this block
    const task2 = false; // Scoped only inside this block
  }

  return [task, task2];
}
