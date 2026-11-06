"""Batch 2: 50 more doctor-founded aesthetic / dermatology / cosmetic dental clinics in the UAE.
Same columns and fit scale as batch 1. No clinic from batch 1 is repeated."""
import build_batch1 as b1

ROWS = [
    # ---------- Aesthetic / dermatology : Dubai ----------
    ("Dr. Azita Ahmadi", "Serenity Aesthetic Clinic", "Regenerative aesthetics", "Dubai", "https://serenity.ae", "Founder & Aesthetic Doctor (clinic site)", "https://serenity.ae/", "A", "Regenerative / longevity niche, which suits a science-led brand"),
    ("Dr. Amina Nabil", "La Vogue Experts Clinic", "Aesthetic eye surgery / injectables / longevity", "Dubai", "", "Founder (Gulf News feature)", "https://gulfnews.com/uae/health/emirati-surgeon-builds-uae-aesthetics-success-story-1.500606052", "A", "Emirati woman surgeon-entrepreneur: ideal women-in-leadership story"),
    ("Dr. Nouf Al Raeesi", "Estelaza Clinic", "Aesthetic medicine", "Dubai", "https://estelaza.com", "Founder (clinic listing)", "https://visitrasalkhaimah.com/blog/best-beauty-clinics-in-uae", "A", "Emirati woman founder, family-medicine background"),
    ("Dr. Ibrahim Galadari", "Galadari Derma Clinic", "Dermatology", "Dubai – Al Thanya St", "https://www.galadariclinic.com", "Head of own private practice (Wikipedia + clinic site)", "https://www.galadariclinic.com/ibrahim.html", "A", "Emirati professor, chairs Dubai Derma: authority-brand angle"),
    ("Dr. Asima Nasir", "Orskin Aesthetics & Fitness Lounge", "Aesthetic medicine", "Dubai", "", "Medical Director; co-founded with Orsi Matheisz (GRAZIA): VERIFY her ownership share", "https://graziamagazine.com/me/articles/best-aesthetics-clinics-dubai-orskin/", "B", ""),
    ("Dr. Mahaveer Mehta", "Skin Laser Dubai (Dr. Mahaveer Mehta Medical Centre)", "Dermatology / laser", "Dubai", "https://skinlaserdubai.com", "Chairman & Medical Director of own centre since 1990", "https://skinlaserdubai.com/", "B", "Legacy practice; pitch modernisation + AI booking"),
    ("Dr. Rawan Al-Dabagh", "Dr. Rawan Clinic", "Dermatology", "Dubai – Jumeirah & Dubai Hills", "", "Doctor-named clinic (listicle): VERIFY", "https://www.best5.ae/5-dermatologists-in-dubai-for-skincare", "B", "US-board dermatologist; check IG, may already be strong"),
    ("Dr. Waqar Maqsood", "Sculpt Roots Medical Clinic", "Dermatology / hair transplant", "Dubai", "https://sculptroots.com", "Leads the clinic (clinic site): VERIFY ownership", "https://sculptroots.com/about-hair-transplant-dubai/", "B", ""),
    ("Dr. Usman Bashir Tahir (Dr. OBT)", "Halcyon Aesthetics Dubai", "Aesthetic / plastic surgery", "Dubai", "https://halcyonaestheticsdubai.com", "Founder & Medical Director (clinic site)", "https://halcyonaestheticsdubai.com/meet-the-team/", "B", "Part of Halcyon Group (since 2001)"),
    ("Dr. Lubna (surname TBC)", "Nyle Skin", "Aesthetic & skin care", "Dubai – Mirdif", "https://nyleskin.com", "Co-founder & CEO (search result)", "https://nyleskin.com/", "B", "Mirdif: check pricing to confirm budget"),
    ("Dr. Ahmad Al-maadarani", "Ecla Clinic", "Dermatology / cosmetology", "Dubai – Umm Suqeim 2", "https://eclaclinic.com", "Lead dermatologist (clinic site): VERIFY founder", "https://eclaclinic.com/", "B", ""),
    ("Dr. Maria Karakoulaki", "Gýneco Clinic", "Aesthetic & functional gynaecology", "Dubai", "https://gyneco.me", "Founder (clinic site)", "https://gyneco.me/the-story-behind-dr-maria-karakoulaki-and-dubais-first-aesthetic-gynaecology-clinic/", "B", "Aesthetics-adjacent; women's health + menopause: strong fit with your ICP"),
    ("Dr. Mariam Al-Farsi", "Dermanostics Clinic", "Dermatology", "Dubai", "https://dermanostics.ae", "Founder, est. 2026 (clinic site): VERIFY, new clinic", "https://dermanostics.ae/about-dermanostics/", "B", "Brand-new clinic, so needs brand from scratch"),
    ("Dr. Dany Kayle", "Dr Kayle Aesthetic Clinic", "Plastic surgery / aesthetics / dermatology", "Dubai – Umm Suqeim 2, Al Wasl Rd", "https://drkayleclinic.com", "Founder & CEO, est. 2000 (clinic site)", "https://drkayleclinic.com/our-clinic/", "C – elite", "Well-known name; AI systems pitch more than branding"),
    ("Dr. Firas Hamdan", "Highness Clinics", "Plastic surgery / dermatology", "Dubai – Healthcare City", "https://www.highnessclinics.ae", "Founder (clinic listing)", "https://www.highnessclinics.ae/", "C – elite", "GRAZIA-featured; likely already has an agency"),
    ("Dr. Alexandre Duvernois", "Apogée Clinic", "Aesthetic medicine", "Dubai – JBR", "", "Listed aesthetic physician (Practo): VERIFY ownership", "https://www.practo.com/dubai/aesthetic-medicine/jumeirah-lakes-towers", "B", "French aesthetic doctor"),
    # ---------- Aesthetic / dermatology : Abu Dhabi ----------
    ("Dr. Nahla Fares", "Cosmedics Skin & Laser Clinic", "Dermatology / laser", "Abu Dhabi", "https://cosmedicsad.com", "Founder (clinic site)", "https://cosmedicsad.com/", "A", "Board-certified dermatologist, woman founder"),
    ("Dr. Khadija Al Zaabi", "House of Skincare", "Dermatology", "Abu Dhabi – Yas Island", "https://houseofskincare.ae", "Leads clinic (clinic site): VERIFY founder", "https://houseofskincare.ae/", "A", "Emirati consultant dermatologist, 21+ yrs"),
    ("Dr. Erfan Rahmani", "Dr. Erfan Rahmani Aesthetics", "Aesthetic medicine", "Abu Dhabi – Rabdan", "https://drerfanrahmani.com", "Doctor-named solo practice (site)", "https://drerfanrahmani.com/", "A", "Solo doctor brand: personal branding is the product"),
    ("Dr. Sherif Mattar", "SkinMed Medical Center", "Aesthetic dermatology", "Abu Dhabi (incl. Musaffah)", "https://drsmmc.com", "Founder (clinic site)", "https://drsmmc.com/our_services/dr-sherif-mattar/", "B", "Musaffah branch is lower-tier; check main branch"),
    ("Dr. Khaled M. Othman", "Skin & Slim Medical Center", "Dermatology / body contouring", "Abu Dhabi", "https://www.skinandslimcenter.com", "Guiding figure on About page: VERIFY founder", "https://www.skinandslimcenter.com/about-us", "B", ""),
    # ---------- Cosmetic dentistry : Dubai ----------
    ("Dr. Antoine Habib & Dr. Salma Alsebaei", "A&S (Antoine & Salma) Dental Clinic", "Cosmetic / orthodontic / surgical dentistry", "Dubai – Al Wasl Rd, Al Manara", "https://asclinic.ae", "Founders (clinic site)", "https://asclinic.ae/", "A", "Husband-wife style co-founders: duo brand story"),
    ("Dr. Ajay Juneja", "New York Dental Clinic", "Prosthodontics / digital smile design", "Dubai", "https://nydcdubai.com", "Founder (clinic site)", "https://nydcdubai.com/", "A", "Writes for 3M/Solventum, so has KOL credibility to build on"),
    ("Dr. Munther AlHerani", "Oval Dental Clinic & Lab", "Cosmetic dentistry", "Dubai", "https://drmuntheralherani.com", "Founder (personal site); AEEDC speaker", "https://drmuntheralherani.com/about", "A", "Already has a personal site; IG may need work"),
    ("Dr. Rashida Juzar Ali", "Le Denté", "Cosmetic & neuromuscular dentistry", "Dubai – Jumeirah", "https://ledente.com", "Founder & Owner (clinic site)", "https://ledente.com/", "A", "Woman founder, Hollywood-smile focus"),
    ("Dr. Tanveer Ahmed", "New Ivory Dental & Implant Clinic", "Implants / cosmetic", "Dubai – Business Bay", "https://newivory.ae", "Founder (clinic site + Doctify)", "https://newivory.ae/dr-tanveer-ahmed/", "A", ""),
    ("Dr. Maria Aleksashina", "MedDental (The Dome)", "Cosmetic dentistry", "Dubai – JLT", "https://www.meddental.ae", "Founder, est. 2015", "https://medium.com/@meddentaljlt/meddental-was-founded-by-dr-44caaae13290", "A", "Woman founder"),
    ("Dr. Dominique Caron", "Versailles Dental Clinic", "General & cosmetic dentistry", "Dubai", "https://www.versaillesdentalclinic.com", "Founder, est. 2007 (clinic site)", "https://www.versaillesdentalclinic.com/", "A", "French positioning, premium expat clientele"),
    ("Dr. Maen Aburas", "Dr. Aburas Dental Center", "Implantology / aesthetic dentistry", "Dubai – Al Wasl Rd", "https://aburas.ae", "Founder (clinic site)", "https://aburas.ae/", "A", "Doctor-named centre"),
    ("Dr. Liliia Zhernova", "DentalDate", "Orthodontics / cosmetic", "Dubai – Jumeirah 3", "https://dentaldate.ae", "Founder (clinic site)", "https://dentaldate.ae/", "A", "Woman founder"),
    ("Dr. Khalid Aletaibi", "Dr. Khalid Aletaibi Dental", "Digital smile design", "Dubai – Al Wasl / Jumeirah", "https://khalidaletaibi.com", "Doctor-named practice (site): VERIFY ownership", "https://khalidaletaibi.com/en/dentist-in-al-wasl", "A", ""),
    ("Dr. Manisha Singh", "Top Smile Dental Clinic", "Prosthodontics / cosmetic", "Dubai – Oud Metha & Silicon Oasis", "https://topsmiledentalclinic.com", "Founder, est. Jul 2023 (clinic site)", "https://topsmiledentalclinic.com/about-us/", "B", "New clinic; mid-market areas, so confirm budget"),
    ("Dr. Petros Yuvanoglu", "SameDay Dental Implant Clinic", "Prosthodontics / implants", "Dubai", "https://www.samedayme.com", "Co-founder (clinic blog)", "https://www.samedayme.com/blog/how-did-sameday-dental-implant-clinic-start-in-dubai", "B", "Implant focus, not pure cosmetic"),
    ("Dr. Gilda Behnam & Dr. Mahmoud Dastoori", "Downtown Clinic", "Dental / aesthetic", "Dubai – Downtown", "https://downtownclinic.ae", "Founders, opened 2022 (clinic site)", "https://downtownclinic.ae/", "B", "Confirm specialty mix"),
    ("Dr. Aimen Zia", "Dr. Aimen Zia Dental Clinic", "General & cosmetic dentistry", "Dubai", "https://draimenziadentalclinic.ae", "Doctor-named clinic (site): VERIFY", "https://draimenziadentalclinic.ae/", "B", "Woman dentist, 24/7 clinic"),
    ("Dr. Rena Eva Dean", "Serenity Dental Clinic", "General & cosmetic dentistry", "Dubai – Motor City", "https://serenitydentaldubai.com", "Founder (clinic site)", "https://serenitydentaldubai.com/", "B", "Woman founder"),
    ("Dr. Ibrahim Bin Arab", "Bin Arab Dental Centre", "Dentistry", "Dubai", "http://binarabdentalcentre.com", "Founder (clinic site)", "http://binarabdentalcentre.com/", "B", "Emirati founder"),
    ("Dr. Homa Shahakbari", "Alma Polyclinic", "Dental + gynaecology", "Dubai – Jumeirah", "https://almapolyclinic.com", "Founder, est. 2020 (clinic site)", "https://almapolyclinic.com/about-us/", "B", "Woman founder"),
    ("Dr. Bayan H. Mahboubi", "Mahboubi Poly Dental Clinic", "Orthodontics / dentistry", "Dubai – Al Wasl Rd, Jumeirah 1", "", "Heads family clinic founded 1950 by Dr. Hussain Mahboubi", "https://m.edarabia.com/mahboubi-poly-dental-clinic-jumeirah/3729/", "B", "Heritage story: 'oldest dental clinic in the Gulf' is a strong brand hook"),
    ("Dr. Ehab Rashed", "Dr. Ehab's Dental Clinic", "Implantology / cosmetic", "Dubai – Business Bay", "", "Founder, est. 1997 (directory)", "https://m.edarabia.com/dr-ehabs-dental-clinic/74055/", "B", ""),
    # ---------- Cosmetic dentistry : Abu Dhabi ----------
    ("Dr. Natalia Lola", "True Smile Dental Center", "Orthodontics / cosmetic / implants", "Abu Dhabi – Al Reem Island", "https://truesmile.ae", "Owner & CEO (clinic site)", "https://truesmile.ae/", "A", "Won a 2026 Aesthetic Dentistry MENA award (clinic claim)"),
    ("Dr. Fahad Mohamed", "Smile First Dental Clinic", "Cosmetic dentistry / orthodontics", "Abu Dhabi", "https://smilefirstad.ae", "Founder (clinic site)", "https://smilefirstad.ae/", "B", ""),
    ("Dr. Azzam Al Jundi", "Aljundi Orthodontic & Dental Center", "Orthodontics / dentistry", "Abu Dhabi – Al Karama St", "https://www.draljundi.com", "Established it in 2005 (clinic site)", "https://www.draljundi.com/", "B", ""),
    ("Dr. Musa Jaffal", "French Dental & Aesthetic Center", "Dental + dermatology", "Abu Dhabi – Mohamed Bin Khalifa St", "", "CEO, est. 2002 (directory): VERIFY founder", "https://m.edarabia.com/french-dental-and-aesthetic-center/74114/", "B", ""),
    ("Dr. Mohamed Sharshera", "Dr. Sharshera Dental", "Implantology / cosmetic", "Abu Dhabi", "https://drsharshera.com", "Doctor-named practice (site): VERIFY ownership", "https://drsharshera.com/hollywood-smile/", "B", ""),
    ("Dr. Hussein Salah Tahoun", "Vision Dental Clinic", "Dentistry", "Abu Dhabi – Downtown", "https://visiondentalclinic.com", "Leads clinic (site): VERIFY founder", "https://visiondentalclinic.com/", "B", ""),
    ("Dr. Raj Jaju", "Gentle Dental Care (GDC Abu Dhabi)", "Dentistry / Hollywood smile", "Abu Dhabi", "https://www.gdcabudhabi.ae", "Founder (Mumbai 1983, AD 2001) (clinic site)", "https://www.gdcabudhabi.ae/hollywood-smile.php", "C – elite", "India-based group; AI systems pitch only"),
    # ---------- Al Ain / other ----------
    ("Dr. Maan M. Srour", "Al Andalus Medical Center", "Dental + dermatology", "Al Ain", "https://amc-uae.ae", "Managed by him since 1994 (clinic site)", "https://amc-uae.ae/", "B", "Al Ain's premium end; confirm pricing"),
    ("Dr. Ali Hendawy", "Al Hendawy Medical Center", "Multi-specialty incl. dental + dermatology", "Abu Dhabi", "https://alhendawymc.ae", "Set up by him in 2005 (clinic site)", "https://alhendawymc.ae/", "C – budget?", "Founder is a paediatrician; aesthetics is one department"),
    ("Dr. Lolita M. Lim", "Al Jazeerah Dental Clinic", "Family & cosmetic dentistry", "Sharjah – Al Majaz 3", "https://aljazeeradentalclinic.com", "Founder, est. 1998 (directory)", "https://aljazeeradentalclinic.com/services/hollywood-smile/", "C – budget?", "Sharjah: included only so you can decide; likely below your budget line"),
]

if __name__ == "__main__":
    seen = {r[1].lower() for r in b1.ROWS}
    dupes = [r[1] for r in ROWS if r[1].lower() in seen]
    assert not dupes, dupes
    b1.build(b1.ROWS, "/home/user/Claude-Code/leads/UAE_Doctor_Clinic_Leads_Batch1.xlsx", "Batch 1")
    b1.build(ROWS, "/home/user/Claude-Code/leads/UAE_Doctor_Clinic_Leads_Batch2.xlsx", "Batch 2")
    from collections import Counter
    print(len(ROWS), Counter(r[7][0] for r in ROWS))
