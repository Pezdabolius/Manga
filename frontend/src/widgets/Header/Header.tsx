import { useEffect, useRef, useState } from "react"
import s from "./Header.module.scss"
import { Link, useNavigate } from "react-router-dom"
import { observer } from "mobx-react-lite"

export const Header = observer(() => {
	const [isCatalogOpen, setCatalogOpen] = useState(false)
	const catalogRef = useRef<HTMLLIElement>(null)
	const navigate = useNavigate()

	const handleClickOutside = (event: MouseEvent) => {
		if (catalogRef.current && !catalogRef.current.contains(event.target as Node)) {
			setCatalogOpen(false)
		}
	}

	useEffect(() => {
		document.addEventListener("mousedown", handleClickOutside)
		return () => {
			document.removeEventListener("mousedown", handleClickOutside)
		}
	}, [])

	const toggleCatalogMenu = () => {
		setCatalogOpen(!isCatalogOpen)
	}

	const handleTypeClick = (type: string) => {
		navigate(`/catalog?type=${type}`)
		setCatalogOpen(false)
	}

	return (
		<header className={s.header}>
			<nav className={s.nav}>
				<Link to='/' className={s.nav_brand}>
					MangaApp
				</Link>
				<div className={s.nav_menu}>
					<ul className={s.menu_list}>
						<li ref={catalogRef} onClick={toggleCatalogMenu} className={s.menu_item}>
							Catalog
							{isCatalogOpen && (
								<div className={s.dropdown_catalog}>
									<ul>
										<li onClick={() => handleTypeClick("manga")}>Manga</li>
										<li onClick={() => handleTypeClick("comic")}>Comic</li>
										<li onClick={() => handleTypeClick("manhwa")}>Manhwa</li>
										<li onClick={() => handleTypeClick("manhua")}>Manhua</li>
									</ul>
								</div>
							)}
						</li>
						<li className={s.menu_item}>Search</li>
						<li className={s.menu_item}>Discussion</li>
					</ul>
				</div>
				<div className={s.nav_menu2}>
					<ul>
						<li className={s.nav_sign_in}>Sign In</li>
						<li className={s.nav_sign_up}>Sign Up</li>
						<li className={s.nav_color_theme}>Theme</li>
					</ul>
				</div>
			</nav>
		</header>
	)
})
