import { useEffect } from 'react'
import { mangaStore } from '../../store/api/manga-store/manga-store'
import s from './MainPage.module.scss'
import { GetMangaResponse } from '../../shared/api/mangaApi/types'
import { observer } from 'mobx-react-lite'
import { useNavigate } from 'react-router-dom'

export const MainPage = observer(() => {
	const { mangaData, getMangaAction } = mangaStore
	const navigate = useNavigate()

	useEffect(() => {
		getMangaAction()
	}, [getMangaAction])

	return (
		<div className={s.main}>
			<div className={s.container}>
				{mangaData.state === 'pending' ? (
					<div>Loading...</div>
				) : (
					<>
						{/* @ts-ignore */}
						{mangaData?.value?.data?.map((item: GetMangaResponse) => {
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
										<p className={s.manga_title} onClick={() => navigate(`/manga-item/${item.title}`)}>
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
