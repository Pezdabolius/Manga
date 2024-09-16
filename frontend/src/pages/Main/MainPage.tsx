import { useEffect } from "react"
import { mangaStore } from "../../store/api/manga-store/manga-store"
import s from "./MainPage.module.scss"
import { GetMangaResponse } from "../../shared/api/mangaApi/types"
import { observer } from "mobx-react-lite"

export const MainPage = observer(() => {
	const { mangaData, getMangaAction } = mangaStore

	useEffect(() => {
		getMangaAction()
	}, [getMangaAction])

	return (
		<div className={s.main}>
			<div className={s.container}>
				{mangaData?.state === "pending" ? (
					<span>Loading...</span>
				) : (
					<>
						{Array.isArray(mangaData?.value) ? (
							mangaData.value.map((item: GetMangaResponse) => (
								<div key={item.id}>
									<p>{item.title}</p>
									<p>{item.description}</p>
								</div>
							))
						) : (
							<span>No data available</span>
						)}
					</>
				)}
			</div>
		</div>
	)
})
