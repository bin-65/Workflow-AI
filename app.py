/* Expanded Right Image Side - Fixed Face Alignment */
    .banner-right-img {
        width: 48%;
        position: relative;
        background-image: url('{banner_bg_img}');
        background-size: cover;
        background-position: center 20%; /* Brings Engineer's face into full view */
        background-repeat: no-repeat;
        border-top-right-radius: 16px;
        border-bottom-right-radius: 16px;
    }

    .banner-overlay-badge {
        position: absolute;
        bottom: 12px;
        right: 12px;
        background: rgba(15, 23, 42, 0.85); /* Semi-transparent dark overlay so image stays visible */
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.82rem;
        padding: 6px 14px;
        border-radius: 20px;
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
