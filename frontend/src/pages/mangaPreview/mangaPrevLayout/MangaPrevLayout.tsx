import s from "./MangaPrevLayout.module.scss"

export const MangaPrevLayout = (props: MangaPrevLayoutProps) => {
	return (
		<div className={s.manga}>
			<div className={s.manga_cover_img}>
				<img
					src={`${import.meta.env.VITE_API_URL}${props.manga.background}`}
					alt={props.manga.title}
				/>
			</div>
			<div className={s.manga_prev_descr}>
				<p className={s.manga_title}>{props.manga.title}</p>
				<p className={s.manga_subtitle}>{props.manga.type}</p>
			</div>
		</div>
	)
}

interface Manga {
	background: string
	title: string
	type: string
}

interface MangaPrevLayoutProps {
	manga: Manga
}
