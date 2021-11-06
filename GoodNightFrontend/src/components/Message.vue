<template>
    <div class="message">
        <div class="message-logo" :style="'background-color: ' + levelColor[msg.level]">
            <div>{{ index }}</div>
        </div>
        <div class="message-right">
            <div class="message-time">{{ msg.time }}</div>
            <div class="message-details">
                <!-- <img src="../assets/logo.png" alt=""> -->
                <span v-if="msg.type === 'text'">
                    <span v-html="textToHtml(msg.context)"></span>
                </span>
                <span v-if="msg.type === 'img'">
                    <img :src="msg.context" alt />
                </span>
                <span v-if="msg.type === 'mix'">
                    <span v-for="cxt,idx in mixMsg(msg.context)" :key="idx">
                        <span v-if="cxt.type === 'text'">
                            <span v-html="textToHtml(cxt.context)"></span>
                        </span>
                        <span v-if="cxt.type === 'img'">
                            <img :src="cxt.context" alt />
                        </span>
                        <br />
                    </span>
                </span>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    props: {
        msg: Object,
        index: Number
    },
    data() {
        return {
            selectMsg: this.msg.rowid,
            levelColor: ['gray', 'green', 'red']
        }
    },
    methods: {
        textToHtml(txt) {
            return txt.replaceAll('\n', '<br/>')
        },
        mixMsg(data) {
            // console.log("mixMsg -> ", data)
            const d = JSON.parse(data)
            // console.log(d)
            return d['msg']
        },


    }
}
</script>

<style>
.message {
    width: 100%;
    /* width: 300px; */
    /* height: 200px; */
    /* background-color: gray; */
    display: flex;
}

.message-logo {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin: 5px;
    background-color: green;
}

.message-logo div {
    color: white;
    width: 50px;
    height: 50px;
    line-height: 50px;
}

.message-right {
    width: calc(100% - 60px);
    display: flex;
    flex-direction: column;
}

.message-time {
    width: 100%;
    height: 20px;
    margin: 5px 0;
    text-align: left;
    color: gray;
    font-size: 14px;
    /* background-color: rebeccapurple; */
}

.message-details {
    /* min-width: 20px; */
    /* min-height: 20px; */
    width: fit-content;
    max-width: calc(100% - 100px);
    /* max-height: 500px; */
    padding: 8px;
    text-align: left;
    line-height: 100%;
    border-radius: 10px;
    /* background-color: bisque; */
    background-color: whitesmoke;
}

</style>