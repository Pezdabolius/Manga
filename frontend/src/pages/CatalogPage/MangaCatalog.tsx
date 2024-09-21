import { useEffect } from "react"
import { mangaStore } from "../../store/api/manga-store/manga-store"
import s from "./MangaCatalog.module.scss"
import { observer } from "mobx-react-lite"
import { GetMangaResponse } from "../../shared/api/mangaApi/types"
import { useLocation, useNavigate } from "react-router-dom"

const useQuery = () => {
	return new URLSearchParams(useLocation().search)
}

export const MangaCatalog = observer(() => {
	const { mangaData, getMangaAction } = mangaStore
	const query = useQuery()
	const typeFilter = query.get("type")
	const navigate = useNavigate()

	useEffect(() => {
		getMangaAction()
	}, [getMangaAction])

	/* @ts-ignore */
	const filteredData = mangaData?.value?.data?.filter(
		(item: GetMangaResponse) => item.type.toLowerCase() === typeFilter?.toLowerCase()
	)

	return (
		<div className={s.catalog}>
			<div className={s.container}>
				{mangaData.state === "pending" ? (
					<div>Загрузка...</div>
				) : (
					<>
						{filteredData?.map((item: GetMangaResponse) => {
							const imageUrl = `http://127.0.0.1:8000${item.cover}`
							return (
								<div key={item.id} className={s.manga}>
									<img
										src={imageUrl}
										alt={item.title}
										className={s.manga_img}
										onClick={() => navigate(`/manga-item/${item.title}`)}
									/>
									<div className={s.manga_title_wrapper}>
										<p
											className={s.manga_title}
											onClick={() => navigate(`/manga-item/${item.title}`)}
										>
											{item.title}
										</p>
										<p className={s.manga_type}>{item.type}</p>
									</div>
								</div>
							)
						})}
					</>
				)}
			</div>
		</div>
	)
})
