import { useEffect, useRef, useState } from "react"
import s from "./Header.module.scss"
import { Link, useNavigate } from "react-router-dom"
import { observer } from "mobx-react-lite"

export const Header = observer(() => {
	const [isCatalogOpen, setCatalogOpen] = useState(false)
	const [addMenuOpen, setAddMenuOpen] = useState(false)
	const catalogRef = useRef<HTMLLIElement>(null)
	const addMenuRef = useRef<HTMLLIElement>(null)
	const navigate = useNavigate()

	const handleClickOutside = (event: MouseEvent) => {
		if (catalogRef.current && !catalogRef.current.contains(event.target as Node)) {
			setCatalogOpen(false)
		}
		if (addMenuRef.current && !addMenuRef.current.contains(event.target as Node)) {
			setAddMenuOpen(false)
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

	const toggleAddMenu = () => {
		setAddMenuOpen(!addMenuOpen)
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
						<li ref={addMenuRef} onClick={toggleAddMenu} className={s.menu_item}>
							+
							{addMenuOpen && (
								<div className={s.dropdown_add}>
									<ul>
										<Link to='/add-title'>
											<li>Add Title</li>
										</Link>
										<Link to='/add-author'>
											<li>Add Author</li>
										</Link>
										<Link to='/add-artist'>
											<li>Add Artist</li>
										</Link>
										<Link to='/add-publisher'>
											<li>Add Publisher</li>
										</Link>
									</ul>
								</div>
							)}
						</li>
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
