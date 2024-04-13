/*
  Taken from: https://github.com/VictorTaelin/ab_challenge_eval
  split the data into data.js
  run node app.js > data.json
  modify params in makeQa() to change which questions are created:
  currently creates questions on difficulty level 1-10 (out of 24)
*/

const HA = "#A";
const HB = "#B";
const AH = "A#";
const BH = "B#";

const tokens = [HA,HB,AH,BH];

const instances = require('./data.js')

function reduce(xs) {
    let ys   = [];
    let work = false;
    let rwts = 0;
    for (let i = 0; i < xs.length; i++) {
      if (xs[i] === AH && xs[i+1] === HB) {
        ys.push(HB, AH); i++; rwts++;
      } else if (xs[i] === BH && xs[i+1] === HA) {
        ys.push(HA, BH); i++; rwts++;
      } else if (xs[i] === AH && xs[i+1] === HA) {
        i++; rwts++;
      } else if (xs[i] === BH && xs[i+1] === HB) {
        i++; rwts++;
      } else {
        ys.push(xs[i]);
      }
    }
    return [ys, rwts];
  }
  
  function normal(xs) {
    let rwts = 0;
    let term = xs;
    let work;
    while (true) {
      [term, work] = reduce(term);
      if (work > 0) {
        rwts += work;
      } else {
        break;
      }
    }
    return [term, rwts];
  }
  
  function randomTerm() {
    const result = [];
    for (let i = 0; i < 12; i++) {
      result.push(tokens[Math.floor(Math.random() * tokens.length)]);
    }
    return result;
  }
  
  function show(xs) {
    return xs.map(x => {
      switch (x) {
        case HA: return "#A ";
        case HB: return "#B ";
        case AH: return "A# ";
        case BH: return "B# ";
        default: return "";
      }
    }).join('');
  }

function makeQa(total = 10) {
    qa_pairs = []
    for (let i = 0; i < total; i++) {
        
        diff_num = i
        q_num = 0
        
        const problem = instances[diff_num][q_num]  
        const solution = normal(problem)
        qa_pairs.push({
            problem: show(problem),
            solution: show(solution[0]),
        });

    }
    return qa_pairs
}

data = makeQa()

console.log(JSON.stringify(data, null, 2))


