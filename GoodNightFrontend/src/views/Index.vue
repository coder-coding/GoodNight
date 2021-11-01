<template>
  <div class="Index">
    <el-container>
      <Menu></Menu>
      <el-container>
        <!-- <router-view></router-view> -->
        <keep-alive>
          <router-view v-if="$route.meta.keepAlive"></router-view>
        </keep-alive>
        <router-view v-if="!$route.meta.keepAlive"></router-view>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import Menu from '../components/Menu.vue';
</script>

<style>
</style>
