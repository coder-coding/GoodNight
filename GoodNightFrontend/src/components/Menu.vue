<template>
  <div class="menu">
    <el-button style="width:100%" @click="isCollapse = !isCollapse">
      <i class="el-icon-s-fold" style="font-size:16px"></i>
    </el-button>
    <el-menu default-active="1" :collapse="isCollapse" router>
      <el-menu-item v-for="(item,idx) in menuList" :key="idx" :index="'/index/' + item.name">
        <i class="el-icon-document"></i>
        <template #title>{{ item.name }}</template>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { Projects } from "../Api/Api"
export default {
  created() {
    Projects()
      .then((response) => {
        console.log(response["data"]);
        this.menuList = response.data.data
      })
      .catch((error) => {
        console.log(error);
      });
  },
  data() {
    return {
      isCollapse: false,
      menuList: [
        {
          name: 'adddddddddddddaa',

        },
        {
          name: 'bbb',

        }
      ]
    }
  }
}
</script>

<style>
.el-menu {
  border-right: none;
}

.menu {
  height: 100vh;
  background-color: white;
}

.menu .el-button {
  border-radius: unset;
}
</style>