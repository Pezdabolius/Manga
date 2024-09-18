import { useState } from "react"
import s from "./Header.module.scss"
import { Link } from "react-router-dom"
import { observer } from "mobx-react-lite"

export const Header = observer(() => {
	const [isCatalogOpen, setCatalogOpen] = useState(false)
	const [isCatalogOpen2, setCatalogOpen2] = useState(false)

	const toggleCatalogMenu = () => {
		setCatalogOpen(!isCatalogOpen)
	}
	const toggleCatalogMenu2 = () => {
		setCatalogOpen2(!isCatalogOpen2)
	}

	return (
		<header className={s.header}>
			<nav className={s.nav}>
				<Link to='/' className={s.nav_brand}>
					MangaApp
				</Link>
				<div className={s.nav_menu}>
					<ul className={s.menu_list}>
						<li onClick={toggleCatalogMenu} className={s.menu_item}>
							catalog
							{isCatalogOpen && (
								<div className={s.dropdown_catalog}>
									<ul>
										<li>manga</li>
										<li>comic</li>
									</ul>
								</div>
							)}
						</li>
						<li className={s.menu_item}>search</li>
						<li className={s.menu_item}>discussion</li>
						<li onClick={toggleCatalogMenu2} className={s.menu_item}>
							...
							{isCatalogOpen2 && (
								<div className={s.dropdown_add_author}>
									<ul>
										<Link to='/add-author'>
											<li>Add Author</li>
										</Link>
										<Link to='/add-artist'>
											<li>Add Artist</li>
										</Link>
										<Link to='/create-team'>
											<li>Create Team</li>
										</Link>
									</ul>
								</div>
							)}
						</li>
					</ul>
				</div>
				<div className={s.nav_menu2}>
					<ul>
						<li className={s.nav_sign_in}>sign in</li>
						<li className={s.nav_sign_up}>sign up</li>
						<li className={s.nav_color_theme}>theme</li>
					</ul>
				</div>
			</nav>
		</header>
	)
})
