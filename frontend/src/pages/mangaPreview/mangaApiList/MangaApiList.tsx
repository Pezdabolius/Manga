import { useEffect, useState } from "react"
import s from "./MangaApiList.module.scss"
import axios from "axios"
import { MangaPrevLayout } from "../mangaPrevLayout/MangaPrevLayout"

export const MangaApiList = () => {
	const [mangaListData, setMangaListData] = useState<Manga[]>([])

	const mangaResponse = `${import.meta.env.VITE_API_URL}/api/manga_list/`

	const fetchData = async () => {
		const response = await axios.get<Manga[]>(mangaResponse)
		const { data } = response
		setMangaListData(data)
		return data
	}

	useEffect(() => {
		fetchData()
	}, [])

	return (
		<div className={s.manga}>
			{mangaListData.map((manga) => (
				<MangaPrevLayout manga={manga} key={manga.id} />
			))}
		</div>
	)
}

interface Manga {
	id: number
	background: string
	title: string
	type: string
}
