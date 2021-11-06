<template>
    <div class="msg-box" @click="msgClick">
        <Message
            v-for="msg,idx in messageList"
            :key="idx"
            :msg="msg"
            :index="messageList.length - idx"
            @contextmenu="contextmenu($event, idx)"
        ></Message>
        <div id="msgmenu">
            <span @click="toClipboard(messageList[selectMsg].context)">复制</span>
            <span @click="delMsg">删除</span>
            <span @click="msgLevel(0)">标记为普通消息</span>
            <span @click="msgLevel(1)">标记为成功消息</span>
            <span @click="msgLevel(2)">标记为失败消息</span>
        </div>
    </div>
</template>

<script>
import { level, del } from '../Api/Api'
import { toClipboard } from '@soerenmartius/vue3-clipboard'
import { toRefs } from '@vue/reactivity'
export default {
    props: {
        messageList: Object,
        project: String
    },
    data() {
        return {
            // messageList:
            // [
            //     {
            //         type: 'text',
            //         level: 0,
            //         time: '2021/10/28 15:05:06',
            //         context: '哈\n哈哈哈哈哈哈\n哈哈哈哈哈哈哈\n哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈'
            //     },
            //     {
            //         type: 'img',
            //         level: 1,
            //         time: '2021/10/28 15:05:08',
            //         context: '../src/assets/logo.png'
            //     },
            //     {
            //         type: 'mix',
            //         level: 2,
            //         time: '2021/10/28 15:05:08',
            //         context: [{ type: 'img', context: '../src/assets/logo.png' }, { type: 'text', context: 'hh\nhhhhh' }, { type: 'img', context: '../src/assets/logo.png' }, { type: 'text', context: 'hhhhhhh' }]
            //     }
            // ]
            selectMsg: -1
        }
    },
    methods: {
        contextmenu(v, idx) {
            v.preventDefault()
            const dom = document.getElementById('msgmenu')
            dom.style.display = 'block'
            dom.style.left = v.clientX + 'px'
            dom.style.top = v.clientY + 'px'
            this.selectMsg = idx
            console.log(this.selectMsg)
        },
        msgClick() {
            const dom = document.getElementById('msgmenu')
            if (dom.style.display !== 'none') {
                dom.style.display = 'none'
            }
        },
        msgLevel(l) {
            // console.log(this.selectMsg)
            level(this.messageList[this.selectMsg].rowid, l)
                .then((response) => {
                    if (response.data.success) {
                        // console.log('true')
                        this.messageList[this.selectMsg].level = l
                    } else {
                        console.log('false')
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        delMsg() {
            del(this.messageList[this.selectMsg].rowid)
                .then((response) => {
                    if (response.data.success) {
                        console.log('del success', this.messageList[this.selectMsg].rowid)
                        this.messageList.splice(this.selectMsg, 1)
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    }
}
</script>

<script setup>
import Message from './Message.vue';
</script>

<style>
.msg-box {
    width: calc(100% - 40px);
    height: calc(100vh - 180px);
    background-color: white;
    border-radius: 1%;
    box-shadow: 5px 5px 20px;
    overflow: scroll;
    padding: 20px;
}
.msg-box::-webkit-scrollbar {
    width: 0 !important;
}
.msg-box {
    -ms-overflow-style: none;
}
.msg-box {
    overflow: -moz-scrollbars-none;
}

#msgmenu {
    height: fit-content;
    width: 150px;
    background-color: ghostwhite;
    border-radius: 10px;
    position: absolute;
    display: none;
}

#msgmenu span {
    display: block;
    height: 30px;
    line-height: 30px;
    border-bottom: 1px solid white;
}

#msgmenu span:hover {
    background-color: whitesmoke;
    cursor: pointer;
}
</style>