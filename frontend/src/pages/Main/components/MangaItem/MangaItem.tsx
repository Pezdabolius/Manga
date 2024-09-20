import { useEffect, useState } from 'react'
import s from './MangaItem.module.scss'
import { observer } from 'mobx-react-lite'
import { Link, useParams } from 'react-router-dom'
import { getManga } from '../../../../shared/api/mangaApi/api'
import { GetMangaResponse } from '../../../../shared/api/mangaApi/types'

export const MangaItem = observer(() => {
	const params = useParams<{ title: string }>()
	const [manga, setManga] = useState<GetMangaResponse | null>(null)
	const [loading, setLoading] = useState(true)
	const [error, setError] = useState<string | null>(null)

	useEffect(() => {
		const fetchManga = async () => {
			setLoading(true)
			try {
				const response = await getManga()
				const mangaList: GetMangaResponse[] = response.data
				const selectedManga = mangaList.find((item) => item.title === params.title)

				if (selectedManga) {
					setManga(selectedManga)
				} else {
					setError('Манга не найдена')
				}
			} catch (err) {
				setError('Ошибка при получении данных')
			} finally {
				setLoading(false)
			}
		}

		fetchManga()
	}, [params.title])

	if (loading) return <div>Загрузка...</div>
	if (error) return <div>{error}</div>
	if (!manga) return null

	return (
		<div className={s.main}>
			<div className={s.container}>
				<div className={s.blocks}>
					<div className={s.left}>
						<div className={s.left_img}>
							<img src={`http://127.0.0.1:8000${manga.cover}`} alt={manga.title} className={s.left_back_image} />
						</div>
						<button className={s.left_btn_read}>READ CHAPTER LIST</button>
						<div className={s.left_types_info}>
							<div className={s.left_types_wrap}>
								<div className={s.left_types_info_subtitle}>Type</div>
								<div className={s.left_types_info_title}>{manga.type}</div>
							</div>
							<div className={s.left_types_wrap}>
								<div className={s.left_types_info_subtitle}>Status</div>
								<div className={s.left_types_info_title}>{manga.status}</div>
							</div>
							<div className={s.left_types_wrap}>
								<div className={s.left_types_info_subtitle}>Author</div>
								<div className={s.left_types_info_title}>{manga.author}</div>
							</div>
							<div className={s.left_types_wrap}>
								<div className={s.left_types_info_subtitle}>Artist</div>
								<div className={s.left_types_info_title}>{manga.artist}</div>
							</div>
							<div className={s.left_types_wrap}>
								<div className={s.left_types_info_subtitle}>Release</div>
								<div className={s.left_types_info_title}>{manga.release}</div>
							</div>
							<div className={s.left_types_wrap}>
								<div className={s.left_types_info_subtitle}>Publisher</div>
								<div className={s.left_types_info_title}>{manga.publisher}</div>
							</div>
							<div className={s.left_types_wrap}>
								<div className={s.left_types_info_subtitle}>Rating</div>
								<div className={s.left_types_info_title}>{manga.rating}</div>
							</div>
						</div>
					</div>
					<div className={s.right}>
						<div className={s.tabs}>
							<Link to='/manga-tab-info' className={s.tab}>
								Manga Info
							</Link>
							<Link to='/manga-tab-chapters' className={s.tab}>
								Manga Chapters
							</Link>
						</div>
						<div className={s.right_title_rating}>
							<div className={s.right_title}>{manga.title}</div>
							<div className={s.right_title}>rating: 9/10</div>
						</div>
						<div className={s.right_content}>
							<div className={s.right_content_descr}>{manga.description}</div>
							<div className={s.right_content_tags}>
								{manga.tag?.map((tag) => (
									<div key={tag} className={s.tag}>
										{tag}
									</div>
								))}
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	)
})
