<template>
  <div class="header">
    <el-page-header icon="el-icon-view" title="查看日志" :content="project"></el-page-header>
  </div>
</template>

<script>
import { ref, toRefs } from '@vue/reactivity'
export default {
  props: {
    project: String
  },
  setup(props) {

    console.log(props)
    const { project } = toRefs(props)
    return {
      project
    }
  },
}
</script>

<style>
.header {
  margin: 0 10px 15px 10px;
  display: contents;
}
</style>