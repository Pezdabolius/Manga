import { MangaApiList } from "../mangaPreview/mangaApiList/MangaApiList"
import s from "./Home.module.scss"

export const Home = () => {
	return (
		<div className={s.home}>
			<div className={s.container}>
				<div className={s.content}>
					<MangaApiList />
				</div>
			</div>
		</div>
	)
}
