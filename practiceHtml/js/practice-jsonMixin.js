/**
 *
 * by littlefean
 */
window.onload = function () {

    let wordListJson = [
            {
                "name": "understand",
                "chinese": "v.懂,理解;获悉,听说;揣测,认为",
                "chineseList": [
                    "懂",
                    "理解",
                    "获悉",
                    "听说",
                    "揣测",
                    "认为"
                ]
            },
            {
                "name": "twice",
                "chinese": "ad.两次,两倍",
                "chineseList": [
                    "两次",
                    "两倍"
                ]
            },
            {
                "name": "them",
                "chinese": "pron.他们",
                "chineseList": [
                    "pro他们"
                ]
            },
            {
                "name": "pleasant",
                "chinese": "a.令人愉快的 vt.使高兴 vi.满意；喜欢",
                "chineseList": [
                    "令人愉快的 使高兴 满意",
                    "喜欢"
                ]
            },
            {
                "name": "tentative",
                "chinese": "a.试探性的，暂时的；犹豫不决的",
                "chineseList": [
                    "试探性的",
                    "暂时的",
                    "犹豫不决的"
                ]
            },
            {
                "name": "prison",
                "chinese": "n.监狱",
                "chineseList": [
                    "监狱"
                ]
            },
            {
                "name": "accident",
                "chinese": "n.意外遭遇,事故；意外(因素)",
                "chineseList": [
                    "意外遭遇",
                    "事故",
                    "意外(因素)"
                ]
            },
            {
                "name": "doze",
                "chinese": "v.",
                "chineseList": [
                    ""
                ]
            },
            {
                "name": "radioactive",
                "chinese": "a.放射性,放射引起的",
                "chineseList": [
                    "放射性",
                    "放射引起的"
                ]
            },
            {
                "name": "collect",
                "chinese": "v.收集,搜集;领取,接走;收(税等);聚集,堆积",
                "chineseList": [
                    "收集",
                    "搜集",
                    "领取",
                    "接走",
                    "收(税等)",
                    "聚集",
                    "堆积"
                ]
            },
            {
                "name": "sustain",
                "chinese": "vt.支撑,撑住;维持,持续,经受,忍耐",
                "chineseList": [
                    "支撑",
                    "撑住",
                    "维持",
                    "持续",
                    "经受",
                    "忍耐"
                ]
            },
            {
                "name": "hurricane",
                "chinese": "n.飓风",
                "chineseList": [
                    "飓风"
                ]
            },
            {
                "name": "integrity",
                "chinese": "n.正直,诚实;完整,完全",
                "chineseList": [
                    "正直",
                    "诚实",
                    "完整",
                    "完全"
                ]
            },
            {
                "name": "glorious",
                "chinese": "a.壮丽的,辉煌的;光荣的",
                "chineseList": [
                    "壮丽的",
                    "辉煌的",
                    "光荣的"
                ]
            },
            {
                "name": "university",
                "chinese": "n.(综合)大学",
                "chineseList": [
                    "(综合)大学"
                ]
            },
            {
                "name": "back",
                "chinese": "a.后面的 ad.向后 v.倒退；支持 n.背；后面",
                "chineseList": [
                    "后面的 向后 倒退",
                    "支持 背",
                    "后面"
                ]
            },
            {
                "name": "lung",
                "chinese": "n.肺",
                "chineseList": [
                    "肺"
                ]
            },
            {
                "name": "means",
                "chinese": "n.方法,手段",
                "chineseList": [
                    "方法",
                    "手段"
                ]
            },
            {
                "name": "eject",
                "chinese": "v.喷射,排出;驱逐",
                "chineseList": [
                    "喷射",
                    "排出",
                    "驱逐"
                ]
            },
            {
                "name": "scenery",
                "chinese": "n.风景,舞台布景",
                "chineseList": [
                    "风景",
                    "舞台布景"
                ]
            },
            {
                "name": "partly",
                "chinese": "ad.部分地,不完全地,在一定程度上",
                "chineseList": [
                    "部分地",
                    "不完全地",
                    "在一定程度上"
                ]
            },
            {
                "name": "grocer",
                "chinese": "n.食品商,杂货商",
                "chineseList": [
                    "食品商",
                    "杂货商"
                ]
            },
            {
                "name": "vegetable",
                "chinese": "n.蔬菜,植物 a.植物的,蔬菜的",
                "chineseList": [
                    "蔬菜",
                    "植物 植物的",
                    "蔬菜的"
                ]
            },
            {
                "name": "pair",
                "chinese": "n.一对,一双;一副;夫妇 v.配对,成对",
                "chineseList": [
                    "一对",
                    "一双",
                    "一副",
                    "夫妇 配对",
                    "成对"
                ]
            },
            {
                "name": "physics",
                "chinese": "n.物理(学)",
                "chineseList": [
                    "物理(学)"
                ]
            },
            {
                "name": "impossible",
                "chinese": "a.不可能的；难以忍受的，很难对付的",
                "chineseList": [
                    "不可能的",
                    "难以忍受的",
                    "很难对付的"
                ]
            },
            {
                "name": "thorough",
                "chinese": "a.彻底的,完全的;精心的",
                "chineseList": [
                    "彻底的",
                    "完全的",
                    "精心的"
                ]
            },
            {
                "name": "latitude",
                "chinese": "n.纬度,行动或言论的自由(范围),(pl.)地区",
                "chineseList": [
                    "纬度",
                    "行动或言论的自由(范围)",
                    "(pl.)地区"
                ]
            },
            {
                "name": "myth",
                "chinese": "n.神话;虚构的理论",
                "chineseList": [
                    "神话",
                    "虚构的理论"
                ]
            },
            {
                "name": "sideways",
                "chinese": "ad.",
                "chineseList": [
                    ""
                ]
            },
            {
                "name": "adventure",
                "chinese": "n.冒险，冒险活动，奇遇 vt.大胆进行",
                "chineseList": [
                    "冒险",
                    "冒险活动",
                    "奇遇 大胆进行"
                ]
            },
            {
                "name": "intersection",
                "chinese": "n.相交，交叉；道路交叉口，十字路口",
                "chineseList": [
                    "相交",
                    "交叉",
                    "道路交叉口",
                    "十字路口"
                ]
            },
            {
                "name": "store",
                "chinese": "n.商店,店铺;贮藏,贮备品 v.贮藏,贮备",
                "chineseList": [
                    "商店",
                    "店铺",
                    "贮藏",
                    "贮备品 贮藏",
                    "贮备"
                ]
            },
            {
                "name": "deposit",
                "chinese": "v.存放;使沉淀;付(保证金) n.存款;沉积物",
                "chineseList": [
                    "存放",
                    "使沉淀",
                    "付(保证金) 存款",
                    "沉积物"
                ]
            },
            {
                "name": "go",
                "chinese": "v.去，离开；走；放置；变成；运转 n.围棋",
                "chineseList": [
                    "去",
                    "离开",
                    "走",
                    "放置",
                    "变成",
                    "运转 围棋"
                ]
            },
            {
                "name": "despatch",
                "chinese": "n.",
                "chineseList": [
                    ""
                ]
            },
            {
                "name": "little",
                "chinese": "a.小，幼小；不多的 ad.",
                "chineseList": [
                    "小",
                    "幼小",
                    "不多的"
                ]
            },
            {
                "name": "inward",
                "chinese": "ad.向内,在内 a.向内的,在内的,里面的",
                "chineseList": [
                    "向内",
                    "在内 向内的",
                    "在内的",
                    "里面的"
                ]
            },
            {
                "name": "wet",
                "chinese": "a.湿的,潮湿的;有雨的,多雨的 v.弄湿,沾湿",
                "chineseList": [
                    "湿的",
                    "潮湿的",
                    "有雨的",
                    "多雨的 弄湿",
                    "沾湿"
                ]
            },
            {
                "name": "hospitality",
                "chinese": "n.好客,殷勤,款待",
                "chineseList": [
                    "好客",
                    "殷勤",
                    "款待"
                ]
            },
            {
                "name": "allocate",
                "chinese": "v.分配，分派；拨给；划归",
                "chineseList": [
                    "分配",
                    "分派",
                    "拨给",
                    "划归"
                ]
            },
            {
                "name": "spiritual",
                "chinese": "a.精神(上)的,心灵的",
                "chineseList": [
                    "精神(上)的",
                    "心灵的"
                ]
            },
            {
                "name": "nightmare",
                "chinese": "n.恶梦；可怕的事物，无法摆脱的恐惧",
                "chineseList": [
                    "恶梦",
                    "可怕的事物",
                    "无法摆脱的恐惧"
                ]
            },
            {
                "name": "prevalent",
                "chinese": "a.流行的,普遍的",
                "chineseList": [
                    "流行的",
                    "普遍的"
                ]
            },
            {
                "name": "manufacture",
                "chinese": "v.制造,加工 n.制造,制造业;产品",
                "chineseList": [
                    "制造",
                    "加工 制造",
                    "制造业",
                    "产品"
                ]
            },
            {
                "name": "transfer",
                "chinese": "vt.",
                "chineseList": [
                    ""
                ]
            }
        ]
    ;
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

