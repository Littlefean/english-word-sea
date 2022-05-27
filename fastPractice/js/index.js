/**
 * 每过3s展示一个单词
 * 先打乱顺序
 *
 * 展示一个单词的时候：
 *     3s内如果按空格了，表示知道这个单词的意思
 *     按下空格之后会展示中文意思 显示1s 然后立刻下一个单词
 *
 *     如果没来及按下空格，就会显示2s 然后立刻显示下一个单词
 *
 * by littlefean
 */
function shuff(arr) {
    arr.sort(function () {
        return .5 - Math.random();
    });
}

let BODY = document.querySelector("body");

window.onload = function () {
    /**
     * 夜间按钮处理
     * @type {Element}
     */
    let sBtn = document.querySelector(".switchBtn");
    let isNight = true;
    sBtn.addEventListener("click", () => {
        isNight = !isNight;
        if (isNight) {
            document.body.style.color = "black";
            document.body.style.backgroundColor = "whitesmoke";
        } else {
            document.body.style.color = "whitesmoke";
            document.body.style.backgroundColor = "black";
        }
    })
    document.querySelector(".max").innerHTML = WORD_LIST.length;
    let indexEle = document.querySelector(".index");
    let englishEle = document.querySelector(".eng");
    let chineseEle = document.querySelector(".chinese");
    shuff(WORD_LIST);

    let index = 0;

    /**
     * 随机字体大小
     */
    function changeWordCss() {
        englishEle.style.fontSize = Math.random() * 10 + 50 + "px";
    }

    function indexAdd() {
        index++;
        if (index >= WORD_LIST.length) {
            index = 0;
        }
    }

    function getWord() {
        return WORD_LIST[index];
    }

    // 获取下一个单词对象
    function nextWord() {
        index++;
        if (index >= WORD_LIST.length) {
            index = 0;
        }
        return WORD_LIST[index];
    }


    /**
     * 自动模式
     */
    function autoMode() {
        window.addEventListener("keypress", (ev => {
            if (ev.key === " ") {
                chineseEle.style.display = "block";
            }
        }));
        setInterval(() => {
            let word = nextWord();
            indexEle.innerHTML = index;
            englishEle.innerHTML = word.name;
            chineseEle.innerHTML = word.chinese;
            chineseEle.style.display = "none";
            changeWordCss()
        }, 500);
    }

    let step = 0;

    function _next() {
        switch (step % 2) {
            case 0:
                let word = getWord();
                indexEle.innerHTML = index;
                englishEle.innerHTML = word.name;
                chineseEle.innerHTML = word.chinese;
                chineseEle.style.display = "none";
                changeWordCss()
                break;
            case 1:
                chineseEle.style.display = "block";

                indexAdd();
                break;
        }
        step++;
    }

    function handModeHandler(ev) {
        if (ev.key === " ") {
            _next();
        }
    }

    /**
     * 手动模式
     * 1：显示英文
     * 2：显示英文和中文
     * 3：下一个单词
     */
    function handMode() {
        window.addEventListener("keypress", handModeHandler);
        document.querySelector(".box").addEventListener("onclick", handModeHandler);
    }

    let nextBtn = document.querySelector(".nextBtn");
    nextBtn.onclick = function () {
        _next();
    }

    handMode();
    // autoMode();

}
