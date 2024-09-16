import { makeAutoObservable } from "mobx";
import { fromPromise, IPromiseBasedObservable } from "mobx-utils";
import { GetMangaResponse } from "../../../shared/api/mangaApi/types";
import { getManga } from "../../../shared/api/mangaApi/api";

class MangaStore {

    constructor() {
        makeAutoObservable(this);
    }
    mangaData?: IPromiseBasedObservable<GetMangaResponse[]>;

    getMangaAction = async () => {
        try {
            const promise = getManga();
            this.mangaData = fromPromise(promise);
        } catch (err) {
            console.error('Error in getMangaAction:', err);
        }
    };
}

export const mangaStore = new MangaStore();