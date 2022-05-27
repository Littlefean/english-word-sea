/**
 *
 * by littlefean
 */
window.onload = function () {

    // let wordListJson = null;

    const request = new XMLHttpRequest();

    request.open("get", "json/myJson.json");
    request.send(null);

    request.onload = function () {
        if (request.status === 200) {
            let wordListJson = JSON.parse(request.responseText);
            console.log(wordListJson);

            // 初始化显示
            const SUM = wordListJson.length;
            document.querySelector(".sum").innerHTML = SUM;
            let remain = document.querySelector(".remain");

            /**
             * 构建单词卡牌队列
             * @type {*[]}
             */
            let queue = [];
            for (let word of wordListJson) {
                word.level = 0; // 动态添加level属性
                queue.push(word);
            }
            shuffle(queue);

            /**
             * 构建错误卡牌的列表
             * @type {*[]}
             */
            let wrongArr = [];

            let wordEnglish = document.querySelector(".wordEnglish");
            let chineseStr = document.querySelector(".chineseStr");
            let bg = document.querySelector(".bg");

            let btnOk = document.getElementById("ok");
            let btnNo = document.getElementById("no");
            let wornNum = 0;
            let rightNum = 0;
            btnOk.addEventListener("click", clickOk);
            btnNo.addEventListener("click", clickNo);
            window.addEventListener("keydown", (e) => {
                console.log(e.key);
                switch (e.key) {
                    case "1":
                        clickOk();
                        break;
                    case "2":
                        clickNo();
                        break;
                }
            })

            /**
             * 刷新显示
             */
            function freshShow() {
                if (queue.length > 0) {
                    remain.innerText = queue.length;
                    wordEnglish.innerHTML = queue[0]["name"];
                    chineseStr.innerText = queue[0]["chinese"];
                    document.querySelector(".ok").style.width = `${(rightNum / SUM) * 100}%`;
                    document.querySelector(".no").style.width = `${(wornNum / SUM) * 100}%`;
                }
            }

            freshShow();

            /**
             * 清空显示
             */
            function clearShow() {
                wordEnglish.innerHTML = "---";
                chineseStr.innerText = "---";
            }

            /**
             * 点击了熟练的按钮绑定事件
             */
            function clickOk() {
                clearShow();
                bg.innerHTML = `<div class="inner greenInner"></div>`;
                // remove(wrongArr, queue[0].name);

                // 如果空了，显示已完成
                if (queue.length === 0) {
                    alert("训练完毕了");
                    return;
                }
                if (queue[0].level <= 0) {
                    rightNum++;
                    // 删除队列里第一个元素
                    queue.shift();
                } else {
                    queue[0].level--;
                    moveCard();
                }

                // 刷新显示
                freshShow();
            }

            /**
             * 点击了不熟练的按钮绑定事件
             */
            function clickNo() {
                bg.innerHTML = `<div class="inner redInner"></div>`;
                // wornNum++;
                add(wrongArr, queue[0].name);

                wornNum = wrongArr.length;

                queue[0].level++;
                clearShow();
                moveCard();
                // 刷新显示
                freshShow();
            }

            /**
             * 根据一个单词的熟练度将他放到对应的位置上
             */
            function moveCard() {
                if (queue[0].level <= 0) {
                    queue.shift();
                } else {
                    let levelN = queue[0].level;
                    let card = queue.shift();
                    let insertIndex = (1 / Math.pow(2, levelN)) * (queue.length - 1);
                    insertIndex = Math.floor(insertIndex);
                    console.log("insert", insertIndex);
                    queue.splice(insertIndex, 0, card);
                }
            }
        }
    }
}

/**
 * 列表不重复的里增加了一个str
 */
function add(list, str) {
    for (let item of list) {
        if (item === str) {
            return;
        }
    }
    list.push(str);
}

/**
 * 列表里删除一个指定的元素
 * @param list
 * @param str
 */
function remove(list, str) {
    let index = list.indexOf(str);
    if (index > -1) {
        list.splice(index, 1);
    }
}

/**
 * 打乱数组元素
 * @param arr
 */
function shuffle(arr) {
    arr.sort(function () {
        return .5 - Math.random();
    });
}

