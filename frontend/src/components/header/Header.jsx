import React, { useState } from 'react';
import s from './Header.module.scss';

const Header = () => {
  const [isCatalogOpen, setCatalogOpen] = useState(false);

  const toggleCatalogMenu = () => {
    setCatalogOpen(!isCatalogOpen);
  };

  return (  
      <header className={s.header}>
         <nav className={s.nav}>
            <div className={s.nav_brand}>MangaApp</div>
            <div className={s.nav_menu}>
               <ul className={s.menu_list}>
                  <li onClick={toggleCatalogMenu} className={s.menu_item}>
                     catalog
                     {isCatalogOpen && (
                        <div className={s.dropdown}>
                        <ul>
                           <li>manga</li>
                           <li>comic</li>
                        </ul>
                     </div>
                     )}
                  </li>
                  <li className={s.menu_item}>search</li>
                  <li className={s.menu_item}>discussion</li>
                  <li className={s.menu_item}>...</li>
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
  );
}

export default Header;