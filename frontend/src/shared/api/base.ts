import axios from "axios";

function createInstance() {
    const instance = axios.create({
        baseURL: 'http://localhost:8000/api'
    })

    instance.interceptors.request.use(
        (config) => {
            console.log(config)
            return config
        },
        (error) => { return Promise.reject(error) }
    )

    return instance
}

export const baseInstance = createInstance()