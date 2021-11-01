import axios from 'axios';

axios.defaults.baseURL = "http://localhost:5000/"

export function GetProjectMsg(project, params) {
    return axios.get('get/' + project + '?start=' + params.start + '&end=' + params.end)
}

export function Projects(project) {
    return axios.get('projects')
}

export function UpdateProjectMsg(project) {
    return axios.get('update/' + project)
}