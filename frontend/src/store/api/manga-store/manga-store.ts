import { makeAutoObservable } from 'mobx'
import { fromPromise, IPromiseBasedObservable } from 'mobx-utils'
import { GetMangaResponse } from '../../../shared/api/mangaApi/types'
import { getManga } from '../../../shared/api/mangaApi/api'

class MangaStore {
	constructor() {
		makeAutoObservable(this)
	}
	// @ts-ignore
	mangaData: IPromiseBasedObservable<GetMangaResponse[]> = []

	getMangaAction = async () => {
		try {
			// @ts-ignore
			this.mangaData = fromPromise(getManga())
			// console.log(this.mangaData)
		} catch (err) {
			console.error('Error in getMangaAction:', err)
		}
	}
}

export const mangaStore = new MangaStore()
