import axios from 'axios';

axios.defaults.baseURL = "http://localhost:9999/"

export function GetProjectMsg(project, params) {
    return axios.get('get/' + project + '?start=' + params.start + '&end=' + params.end)
}

export function Projects(project) {
    return axios.get('projects')
}

export function UpdateProjectMsg(project) {
    return axios.get('update/' + project)
}

export function level(id, l) {
    return axios.get('level?' + 'id=' + id + '&' + 'level=' + l)
}

export function del(id, l) {
    return axios.get('delete?' + 'id=' + id)
}
