/**
 * 主要的js文件
 */


/**
 * 在html body 里添加一个线
 * x1 y1 是上面的点 x2 y2 是下面的点
 * y2 必须 ＞ y1
 * x1 ＜ x2 线是 ↘
 * x1 ＞ x2 线是 ↙
 */
function createLineEle(x1, y1, x2, y2, idName) {
    if (y1 > y2) {
        let temp = [x2, y2];
        x2 = x1;
        y2 = y1;
        x1 = temp[0];
        y1 = temp[1];
    }
    let lb = document.createElement("div");
    lb.className = "lineBox";
    lb.id = idName;
    let w = Math.abs(x2 - x1);
    let h = Math.abs(y2 - y1);
    lb.style.width = w + 'px';
    lb.style.height = h + 'px';
    lb.style.left = Math.min(x1, x2) + 'px';
    lb.style.top = y1 + 'px';
    let lineEle = document.createElement("div");
    lineEle.className = "line";
    let a = Math.atan(w / h) * 180 / Math.PI; // 角度
    lineEle.style.transform = `translateX(${w / 2}px)`;  // 先移动，再旋转，再缩放
    if (x1 < x2) {
        // 如果是 ↘ 就带符号 ，如果 ↙ 就正号
        a = -a;
    }
    lineEle.style.transform += `rotate(${a}deg)`;
    lineEle.style.transform += `scaleY(${Math.sqrt(w * w + h * h) / h})`;
    lb.appendChild(lineEle);
    return lb;
}

// 接收json里面的文件数据内容
let samesJson = null;
let wordListJson = null;

let body = document.querySelector("body");

let request1 = new XMLHttpRequest();
request1.open("get", "json/wordList.json");
request1.send(null);

request1.onload = function () {
    if (request1.status === 200) {
        wordListJson = JSON.parse(request1.responseText);
        console.log("for:::", wordListJson);
        let counter = 0;
        for (let w of wordListJson) {
            let wEle = document.createElement("div");
            wEle.className = "word";
            wEle.id = w["name"];
            wEle.innerHTML = w["name"];
            let left = (counter % 30) * 75;
            let top = Math.floor(counter / 20) * 30;
            // wEle.pos = [left, top];
            wEle.style.left = left + 'px';
            wEle.style.top = top + 'px';
            body.appendChild(wEle);
            let chineseEle = document.createElement("div");
            chineseEle.className = "chinese";
            chineseEle.innerHTML = w["chinese"];
            wEle.appendChild(chineseEle);
            counter += 1;
        }
    }
    let r2 = new XMLHttpRequest();
    r2.open("get", "json/toPremiseWordInWord.json");
    r2.send(null);
    r2.onload = function () {
        if (r2.status === 200) {
            samesJson = JSON.parse(r2.responseText);
            console.log("samesJson", samesJson);
            let cssString = "";
            /*
            * #rain:hover ~ #rain-constrain,
            * #rain:hover ~ #rain-refrain {
            *   opacity: 1;
            * }
            *
            * */
            // 开始遍历每一个单词对应此表关系组
            for (let wToWs of samesJson["array"]) {
                if (wToWs["sameWords"].length !== 0) {

                    let cssStartArr = [];
                    let queryEle = document.getElementById(wToWs["word"]["name"]);
                    // queryEle.style.backgroundColor = "skyblue";
                    // 开始遍历对应的每一个单词
                    for (let w of wToWs["sameWords"]) {
                        let matchWordEle = document.getElementById(w["name"]);
                        let lineEle = createLineEle(
                            queryEle.offsetLeft + queryEle.offsetWidth / 2,
                            queryEle.offsetTop + queryEle.offsetHeight / 2,
                            matchWordEle.offsetLeft + matchWordEle.offsetWidth / 2,
                            matchWordEle.offsetTop + matchWordEle.offsetHeight / 2,
                            `${wToWs["word"]["name"]}-${w["name"]}`
                        );
                        cssStartArr.push(`#${wToWs["word"]["name"]}:hover ~ #${wToWs["word"]["name"]}-${w["name"]}`);
                        body.appendChild(lineEle);
                    }
                    cssString += cssStartArr.join(", ") + "{opacity: 1;}";
                }
                console.log(wToWs["word"]["name"]);
            }
            // 把css动画添加到html里
            let cssEle = document.createElement("style");
            cssEle.innerHTML = cssString;
            body.appendChild(cssEle);
            document.querySelector(".loading").innerHTML = "okay";
        }
    }
}


