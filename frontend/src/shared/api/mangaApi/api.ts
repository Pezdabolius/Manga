import { baseInstance } from "../base";

export const getManga = async () => (await baseInstance.get('/manga_list/')).data
