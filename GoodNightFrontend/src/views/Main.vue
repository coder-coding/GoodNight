<template>
  <div class="main">
    <Header :project="project"></Header>
    <el-divider></el-divider>
    <div class="main-options">
      <!-- <div> -->
      <el-tooltip content="开启/关闭实时监控" placement="top">
        <el-switch v-model="updateFlag" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
      </el-tooltip>
      <el-date-picker
        v-model="dateRange"
        type="datetimerange"
        :shortcuts="shortcuts"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
      ></el-date-picker>
    </div>
    <!-- </div> -->
    <el-divider></el-divider>
    <div class="main-msgbox">
      <Msg-box :messageList="messageList[project]" :project="project"></Msg-box>
    </div>
  </div>
</template>

<script>
import { GetProjectMsg, UpdateProjectMsg } from '../Api/Api'
import { dateFormat } from '../utils/utils'
export default {
  created() {
    console.log("created", this.$route.params.project)
    this.messageList[this.project] = []
    this.project = this.$route.params.project
    GetProjectMsg(this.project, {
      start: '2000-01-01 00:00:00',
      end: this.dateFormat("YYYY-mm-dd HH:MM:SS", new Date())
    })
      .then((response) => {
        // console.log(response["data"]);
        if (!(this.project in this.messageList)) { this.messageList[this.project] = [] }
        if (this.messageList[this.project].length === 0) {
          this.messageList[this.project] = response.data.data
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
  beforeRouteUpdate(to, from) {
    // console.log(to, from)
    this.project = to.params.project
    GetProjectMsg(this.project, {
      start: '2000-01-01 00:00:00',
      end: this.dateFormat("YYYY-mm-dd HH:MM:SS", new Date())
    })
      .then((response) => {
        // console.log(response["data"]);
        if (!(this.project in this.messageList)) { this.messageList[this.project] = [] }
        if (this.messageList[this.project].length === 0) {
          this.messageList[this.project] = response.data.data
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
  data() {
    return {
      dateFormat: dateFormat,
      project: null,
      dateRange: null,
      messageList: {},
      updateClock: null,
      updateFlag: false,
      shortcuts: [
        {
          text: '最近12小时',
          value: () => {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 12)
            return [start, end]
          },
        },
        {
          text: '最近一天',
          value: () => {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 1)
            return [start, end]
          },
        },
        {
          text: '最近一周',
          value: () => {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7)
            return [start, end]
          },
        },
      ]
    }
  },
  methods: {

  },
  watch: {
    updateFlag(val) {
      if (!val) {
        clearInterval(this.updateClock)
      } else {
        this.updateClock = setInterval(() => {
          UpdateProjectMsg(this.project)
            .then((response) => {
              // console.log(response["data"]);
              let tmpList = response.data.data.sort(function (a, b) { return a.rowid - b.rowid });
              var idx = -1
              for (let i in tmpList) {
                if (tmpList[i].rowid === this.messageList[this.project][0].rowid) {
                  idx = parseInt(i)
                  break
                }
              }
              for (let i = idx + 1; i < tmpList.length; i++) {
                this.messageList[this.project].unshift(tmpList[i])
              }
              // console.log(this.messageList)
            })
            .catch((error) => {
              console.log(error);
            });
        }, 1000)
      }
    },
    dateRange(time) {
      if (time === null) {
        GetProjectMsg(this.project, {
          start: '2000-01-01 00:00:00',
          end: this.dateFormat("YYYY-mm-dd HH:MM:SS", new Date())
        })
          .then((response) => {
            // console.log(response["data"]);
            if (!(this.project in this.messageList)) { this.messageList[this.project] = [] }
            this.messageList[this.project] = response.data.data
          })
          .catch((error) => {
            console.log(error);
          });
        return
      }
      GetProjectMsg(this.project, {
        start: this.dateFormat("YYYY-mm-dd HH:MM:SS", time[0]),
        end: this.dateFormat("YYYY-mm-dd HH:MM:SS", time[1])
      })
        .then((response) => {
          // console.log(response["data"]);
          if (!(this.project in this.messageList)) { this.messageList[this.project] = [] }
          this.messageList[this.project] = response.data.data
        })
        .catch((error) => {
          console.log(error);
        });
      // console.log(this.dateFormat("YYYY-mm-dd HH:MM:SS", time[0]), this.dateFormat("YYYY-mm-dd HH:MM:SS", time[1]))

    }
  }
}
</script>

<script setup>
import Header from '../components/Header.vue';
import MsgBox from '../components/MsgBox.vue'
</script>

<style>
.main .el-divider--horizontal {
  margin: 5px;
}

.main .main-options {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.main {
  margin: 20px 30px;
  height: calc(100vh - 40px);
  width: 100%;
  display: flex;
  flex-direction: column;
}
</style>