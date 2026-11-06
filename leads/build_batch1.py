"""Batch 1: doctor-founded aesthetic / dermatology / cosmetic dental clinics in the UAE.
Every row was found in a web search in Nov 2026. Founder status is as stated by the
clinic's own site or a press/directory listing (see Source column)."""
from urllib.parse import quote_plus
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

# (doctor, clinic, specialty, emirate/area, website, founder evidence, source, fit, notes)
ROWS = [
    # ---------- Aesthetic / dermatology : Dubai ----------
    ("Dr. Inas Musa", "Perla Dermatology Clinic", "Dermatology / aesthetics", "Dubai – City Walk", "https://perla-dc.com", "Founder & Medical Director (clinic site)", "https://perla-dc.com/", "A", "Premium location, single clinic: good fit for clinic + personal brand"),
    ("Dr. Anwar Al Hammadi", "Dermamed Clinic", "Dermatology", "Dubai – Wafi / Healthcare City", "https://www.dermamed.ae/en/", "Founder (clinic site)", "https://www.dermamed.ae/en/", "A", "Senior Emirati consultant dermatologist; check how active the IG is"),
    ("Dr. Juliane Reuter", "Doctor Reuter Medical Center", "Dermatology / holistic", "Dubai – Umm Suqeim", "https://dr-reuter.clinic", "Founder & consultant dermatologist (clinic site)", "https://dr-reuter.clinic/", "A", "German dermatologist; integrative angle fits your mind-body story"),
    ("Dr. Dany Touma", "SkinExperts Polyclinic", "Dermatology / multi-specialty", "Dubai – Jumeirah 2 (Beach Rd)", "https://skinexperts.ae", "Founder (clinic site); also The Skin Clinic Beirut", "https://skinexperts.ae/", "B", "Established name; pitch AI systems / clinic brand more than personal brand"),
    ("Dr. Maria Angelo-Khattar", "Aesthetica Clinic / Altaderma Clinic & Training Center", "Aesthetic medicine / dermatology", "Dubai – Jumeirah", "https://altaderma.com", "Founder of Altaderma (clinic site); Aesthetica founded Oct 2002 (directory)", "https://www.expatwoman.com/dubai/directory/wellness/clinics/cosmetic-surgery-clinics/client/aesthetica-clinic/aesthetica-0", "B", "Long-established; brand may feel dated, so a refresh pitch could work"),
    ("Dr. Sarah Agha", "Diva Clinic", "Aesthetic & skin", "Dubai – Umm Suqeim", "https://divaclinic.ae", "Founder (search result)", "https://divaclinic.ae/", "A", ""),
    ("Dr. Afschin Ghofrani", "Aestheticon", "Aesthetic medicine", "Dubai", "https://www.aestheticon.ae", "Founder, est. 2012 (site structured data)", "https://www.aestheticon.ae/", "A", ""),
    ("Dr. Samir Tarar", "MediCure Aesthetics", "Aesthetic medicine", "Dubai", "", "Founder (press)", "https://dubainewsweek.com/medicure-aesthetics-drives-growth-in-dubais-cosmetic-medicine-market/", "A", "Also linked to Estheticare Jumeirah; confirm which brand is primary"),
    ("Dr. Mehri Pourkand", "Dr Mehri Aesthetic Clinic", "Aesthetic medicine / laser", "Dubai – Jumeirah", "https://drmehri-aesthetic.com", "Name-brand clinic; aesthetic physician in Dubai since 2004 (clinic site)", "https://drmehri-aesthetic.com/about-us/", "A", "Doctor-named clinic: strong personal-brand opportunity"),
    ("Dr. Ahsan & Dr. Zohaib", "My London Skin Clinic", "Aesthetic medicine", "Dubai – DIFC / Jumeirah Beach Hotel", "https://mylondonskinclinic.ae", "Founders (clinic site)", "https://mylondonskinclinic.ae/about-us/", "B", "Already marketed as the 'Botox Brothers'; check whether their brand is already strong"),
    ("Dr. Lydia Sama", "Symphony Beauty Clinic", "Aesthetic medicine", "Dubai – Business Bay", "https://symphonyclinic.ae", "Listed in founder field (directory): VERIFY", "https://symphonyclinic.ae/", "B", "Founder status not confirmed"),
    ("Dr. Amina Al Amiri", "Dr. Amina Al Amiri Clinic", "Aesthetic / dermatology", "Dubai – Jumeirah", "", "Doctor-named clinic (booking listing)", "https://salonist.io/cs/s/DrAminaAlAmiriClinicJumeirah", "A", "Emirati woman doctor; ideal for women-in-leadership positioning"),
    ("Dr. Victoria (surname TBC)", "Dr. Victoria Medical Center", "Cosmetic dermatology", "Dubai – Jumeirah", "", "Doctor-named clinic (booking listing)", "https://salonist.io/cs/s/DrVICTORIAMedicalCenterDermatologistBotoxFillerAestheticTreatmentCosmeticDermatology-Jumeirah", "B", "Get the full name from the clinic's IG/website"),
    ("Dr. Shirin (Errami)", "Clinica Errami", "Aesthetic / polyclinic", "Dubai – Jumeirah", "", "Doctor-named clinic (booking listing)", "https://salonist.io/cs/s/ClinicaErrami-AestheticClinicinJumeirahMedicalClinicinJumeirahPolyclinicinDubai", "B", "Clinic site says it is led by Dr. Shirin; also does aesthetic gynaecology"),
    ("Dr. Faiez Ghanam", "Dr Faiez Ghanam Clinic", "Dermatology / laser (vitiligo)", "Dubai", "https://drfaiezclinic.com", "Doctor-named clinic (site)", "https://drfaiezclinic.com/", "B", "Medical-derm niche; pitch AI patient systems"),
    ("Dr. Sarah Battikha", "Frame by Sarah Battikha Dermatology Clinic", "Dermatology", "Dubai", "", "Doctor-named clinic (Practo)", "https://www.practo.com/dubai/clinics/aesthetic-dermatologist-clinics", "B", "Check her personal IG first; may already be strong"),
    ("Dr. Iftikhar (TBC)", "Dr Iftikhar Medical Center", "Aesthetic", "Dubai – Jumeirah", "https://drifthikarmedicalcenter.com", "Doctor-named clinic (site)", "https://drifthikarmedicalcenter.com/aesthetic-clinic-in-jumeirah/", "B", "Confirm doctor's full name"),
    ("Dr. Radmila Lukian", "Lucia Clinic", "Aesthetic dermatology", "Dubai – Jumeirah Beach Rd", "https://luciaclinic.com", "Founder & CEO (clinic site)", "https://luciaclinic.com/about-dr-radmila-lukian/", "C – elite", "Celebrity clientele, strong brand already. Probably skip, or pitch AI systems only"),
    ("Dr. Jamuna Pai", "SkinLab", "Cosmetic physician", "Dubai – Al Wasl Rd, Al Manara", "https://skinlab.ae", "Founder (clinic site)", "https://skinlab.ae/jamuna-pai", "C – elite", "Big India brand; Dubai branch. Probably skip"),
    # ---------- Aesthetic / dermatology : Abu Dhabi ----------
    ("Dr. Mohammed Amir", "Aura Aesthetics Dermatology Clinic", "Cosmetic dermatology", "Abu Dhabi – Khalifa City A", "https://aura-aesthetics.ae", "Founder (Doctify profile)", "https://doctify.com/en-ae/specialist/amir-mohamed", "A", "Young clinic (~3 yrs): needs brand"),
    ("Dr. Christeen Youssef", "Everlast Wellness Medical Center", "Aesthetic & dermatology", "Abu Dhabi – Al Bateen", "https://everlastwellness.com", "Founder & Medical Director (clinic site)", "https://everlastwellness.com/", "A", "Premium Al Bateen location"),
    ("Dr. Nawar AlFalasi", "Skin Institute Dermatology Center", "Dermatology", "Abu Dhabi – Khalifa Park area", "https://skininstitutederma.ae", "Founder, opened 2018 (clinic site)", "https://www.theskininstitute.ae/about-us/", "A", "Emirati board-certified dermatologist"),
    ("Dr. Mouza Al Suwaidi", "Emirates Dermatology & Cosmetology Centre (EDCC)", "Dermatology / cosmetology", "Abu Dhabi", "https://edcc.ae", "Established by her (clinic site)", "https://edcc.ae/", "A", "Emirati woman founder, Canadian board: excellent fit"),
    ("Prof. Melike Kibar Öztürk", "Doctor Kibar Clinic", "Dermatology / aesthetics", "Abu Dhabi", "", "Owner & Medical Director (congress bio)", "https://www.meidamcongress.com/speakers-2025/", "A", "Turkish professor-dermatologist; confirm address"),
    ("Dr. Khaled Al Nuaimi", "Dr. Khaled Al Nuaimi Specialized Clinic", "Dermatology / aesthetics", "Dubai + Al Ain (Hili Mall)", "https://drk.ae", "Doctor-named clinic (IMCAS profile + clinic site); founder of MEIDAM congress", "https://www.imcas.com/en/profile/dr-khaled-salem-al-nuaimi", "A", "Emirati; speaks at IMCAS, so speaking-brand angle"),
    ("Dr. Sabah Al Sakban", "Dr. Sabah Al Sakban Medical Center", "Dermatology", "Abu Dhabi – Najda St", "https://myssmc.ae", "Set up by him (clinic site)", "https://myssmc.ae/about-us/", "B", "Senior founder who no longer consults; pitch the clinic brand to management"),
    ("Dr. Rola Al Shahadat", "Charisma Clinics", "Dermatology & aesthetics", "Abu Dhabi, Dubai, Al Ain", "https://charismamedicalgroup.com", "Founder & owner (Gulf News partner content + clinic site)", "https://gulfnews.com/gulfnews/gn-focus/charisma-medical-group-the-highest-level-of-innovation-and-expertise-in-the-medical-cosmetic-field-in-the-gcc-1.1721986099828", "B", "Paid press feature, so they already spend on marketing"),
    # ---------- Cosmetic dentistry : Dubai ----------
    ("Dr. Fatma Al Kaddah", "The Dental Boutique", "Cosmetic dentistry", "Dubai – JLT (MBL Royal)", "https://www.thedentalboutique.ae", "Founder & Cosmetic Dentist (clinic site)", "https://www.thedentalboutique.ae/", "A", "Woman founder, boutique positioning: top fit"),
    ("Dr. Gad (full name TBC)", "Dr. Gad Dental Clinic", "Cosmetic dentistry", "Dubai – Business Bay", "https://doctorgad.com", "Founder & Principal Cosmetic Dentist (clinic site)", "https://doctorgad.com/services/cosmetic-dentistry-dubai/", "A", "Doctor-named clinic, veneers focus"),
    ("Dr. Mahmoud Braiq", "VIP Dental Clinic", "Cosmetic & general dentistry", "Dubai – Business Bay (Marasi Dr)", "https://vipclinicdubai.com", "Founder (clinic site)", "https://vipclinicdubai.com/about-us/", "A", ""),
    ("Dr. Nour Al-Kayem", "Bourgeois Dental Clinic", "Aesthetic dentistry", "Dubai – Sheikh Zayed Rd", "https://www.bourgeoisclinic.com", "CEO, Founder & Lead Dentist (clinic site)", "https://www.bourgeoisclinic.com/", "A", "Premium positioning already in the name"),
    ("Dr. Khurram Asgher", "The Smile Collective", "Aesthetic & restorative dentistry", "Dubai – SZR, The One Tower", "https://thesmilecollective.ae", "Founder (clinic site)", "https://thesmilecollective.ae/", "A", "NYU-trained; strong personal-brand story"),
    ("Dr. Haroon Malik", "Queens Elite Medical Center", "Cosmetic dentistry", "Dubai – Dubai Marina", "https://queenselitemedical.com", "Co-Founder (clinic site)", "https://smile.queenselitemedical.com/", "A", "Already runs paid landing pages, so has a marketing budget"),
    ("Dr. Leila Hariri", "Leila Hariri Dental Clinic", "Family & cosmetic dentistry", "Dubai – Al Wasl Rd", "", "Founder, est. 2019 (Gulf News)", "https://gulfnews.com/uae/people/meet-family-dentist-who-designs-smiles-in-dubai-1.103378118", "A", "Quotes ~AED 100k makeovers, so a high-ticket clinic"),
    ("Dr. Hussain Al Saleh", "Oris Dental Center", "Cosmetic / multi-specialty dentistry", "Dubai – Jumeirah", "https://www.orisdentalcenter.ae", "Founder & Clinical Director, est. 2008 (clinic site)", "https://www.orisdentalcenter.ae/", "A", "1,000+ smile makeovers claimed"),
    ("Dr. Lina Hamdan", "Hollywood Smile Clinic", "Cosmetic dentistry", "Dubai", "", "Founder (directory)", "https://m.edarabia.com/hollywood-smile-clinic/43231/", "A", "Woman founder"),
    ("Dr. Majd Naji", "Liberty Dental Clinic", "Cosmetic dentistry", "Dubai", "", "Founder, est. 1999 (MBRF speaker bio)", "https://mbrf.ae/knowledgesummit/en/speaker/dr-majd-naji", "B", "Established; speaker, so open to authority branding"),
    ("Dr. Islam Eldardir", "Real Smile Dental Clinic", "Cosmetic dentistry", "Dubai", "", "Founder (Doctify)", "https://www.doctify.com/en-ae/specialist/ilam-eldardir", "A", ""),
    ("Dr. Khalid Saeed", "Creative Arts Dental & Aesthetics", "Cosmetic dentistry + in-house lab", "Dubai – Jumeirah 3", "https://creativeartsaesthetic.com", "Co-founder (clinic site)", "https://creativeartsaesthetic.com/dentist-al-barsha/", "A", "Single clinic with own lab, so good margins"),
    ("Dr. AL (full name TBC)", "Dr. AL Dental Clinic", "Implant & cosmetic dentistry", "Dubai – City Walk", "https://dral.ae", "Founder (clinic site)", "https://dral.ae/", "A", "US-board prosthodontist; get full name from site"),
    ("Dr. Omar Fabbro", "Doctor Fabbro Dental", "Cosmetic dentistry", "Dubai – Jumeira St villa", "https://doctorfabbro.com", "Doctor-named practice, since 2016 (site)", "https://doctorfabbro.com/", "A", "Italian cosmetic dentist, boutique villa"),
    ("Dr. Alain Miski", "Dr Miski Dental Clinic", "Periodontics / implants / cosmetic", "Dubai – JLT", "https://drmiski.com", "Doctor-named clinic (site): VERIFY ownership", "https://drmiski.com/", "B", ""),
    ("Dr. Akanksha Srivastava", "cosmeticdentist.ae", "Cosmetic dentistry", "Dubai", "https://cosmeticdentist.ae", "Personal-domain practice: VERIFY ownership", "https://cosmeticdentist.ae/", "B", "Founder status not confirmed"),
    ("Dr. Udita Baralay", "Dental Oasis", "Endodontics / smile makeover", "Dubai – JLT", "https://dentaloasis.ae", "Co-founder (clinic site)", "https://dentaloasis.ae/services/smile-makeover/", "B", ""),
    # ---------- Cosmetic dentistry : Abu Dhabi / RAK ----------
    ("Dr. Emad Wani", "Shadi International Dental Center (SIDC)", "Cosmetic & general dentistry", "Abu Dhabi (6 locations)", "https://sidc.ae", "Founder & CEO (clinic site)", "https://sidc.ae/dental-veneers/", "A", "Multi-branch group with budget; pitch AI booking systems"),
    ("Dr. Samih Al-Bahri", "Al Bahri Dental & Orthodontic Center", "Dental / cosmetic", "Abu Dhabi", "https://albahridental.com", "CEO & Founder, since 1978 (clinic site)", "https://albahridental.com/", "B", "Legacy clinic; pitch rebrand/next generation"),
    ("Dr. Mohamed Atef", "iSmile Dental Center", "Cosmetic dentistry", "Ras Al Khaimah", "https://ismileuae.com", "Founder & lead dental surgeon, est. 2014 (clinic site)", "https://ismileuae.com/", "C – budget?", "RAK: affordability not certain"),
    ("Dr. Joy Antony", "Dr. Joy Dental Clinic", "Cosmetic dentistry group", "Dubai (multi-branch)", "https://drjoydentalclinic.com", "Founder & CEO (clinic site)", "https://drjoydentalclinic.com/our-team/", "C – elite", "Big group, so marketing is likely done in-house. AI systems pitch only"),
    ("Dr. Michael Apa", "APA Aesthetic", "Cosmetic dentistry", "Dubai – Umm Suqeim 2", "https://apaaesthetic.com/locations/dubai/", "Founder (clinic site)", "https://apaaesthetic.com/locations/dubai/", "C – elite", "Celebrity NYC dentist. Skip for personal brand"),
]

HEAD = ["#", "Doctor", "Clinic", "Specialty", "Emirate / Area", "Website", "Instagram (find)", "LinkedIn (find)",
        "WhatsApp / Phone", "Founder evidence", "Source", "Fit (A/B/C)", "Notes / pitch angle", "Status", "Last contact"]

def build(rows, path, title):
    wb = Workbook(); ws = wb.active; ws.title = title
    ws.append(HEAD)
    for i, (doc, clinic, spec, area, site, evidence, src, fit, notes) in enumerate(rows, 1):
        q = f"{doc} {clinic}".replace("(full name TBC)", "").replace("(TBC)", "").replace("(surname TBC)", "").replace("(first name TBC)", "")
        ig = f"https://www.google.com/search?q={quote_plus(q + ' instagram')}"
        li = f"https://www.google.com/search?q={quote_plus(q + ' site:linkedin.com/in')}"
        ws.append([i, doc, clinic, spec, area, site, ig, li, "Check website / Google Maps", evidence, src, fit, notes, "Not contacted", ""])
    bold = Font(bold=True, color="FFFFFF")
    for c in ws[1]:
        c.font = bold; c.fill = PatternFill("solid", fgColor="1F4E5F"); c.alignment = Alignment(wrap_text=True, vertical="center")
    fills = {"A": "E2F0D9", "B": "FFF2CC", "C": "F8CBAD"}
    for r in ws.iter_rows(min_row=2):
        f = fills.get(str(r[11].value)[0])
        if f: r[11].fill = PatternFill("solid", fgColor=f)
        for c in r:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            if isinstance(c.value, str) and c.value.startswith("http"):
                c.hyperlink = c.value; c.font = Font(color="0563C1", underline="single")
        for idx in (6, 7):
            r[idx].value = "Search";
    widths = [4, 24, 30, 22, 24, 28, 10, 10, 18, 34, 14, 10, 40, 14, 12]
    for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
    for r in ws.iter_rows(min_row=2):
        if r[10].value: r[10].value = "Link"
        if r[5].value: pass
    ws.freeze_panes = "C2"; ws.auto_filter.ref = ws.dimensions
    key = wb.create_sheet("Read me")
    for line in [
        ["Fit A", "Doctor-founded, premium area/positioning, brand looks under-developed. Contact first."],
        ["Fit B", "Good, but either founder status needs a quick check or the clinic is older/established."],
        ["Fit C", "Elite/strong brand already, or budget uncertain. Lowest priority (AI-systems pitch only)."],
        ["Instagram / LinkedIn", "Click 'Search' to open a pre-filled Google search. Handles were NOT verified in this batch."],
        ["WhatsApp", "Not collected yet. Most UAE clinics list a WhatsApp button on their site / Google Maps."],
        ["Affordability", "Estimated from location, positioning and pricing signals. Not financial data."],
        ["Source", "Where the founder/owner claim came from (Nov 2026 web search). Self-reported by clinics in most cases."],
    ]: key.append(line)
    key.column_dimensions["A"].width = 22; key.column_dimensions["B"].width = 100
    wb.save(path)

def main():
    build(ROWS, "/home/user/Claude-Code/leads/UAE_Doctor_Clinic_Leads_Batch1.xlsx", "Batch 1")

if __name__ == "__main__":
    build(ROWS, "/home/user/Claude-Code/leads/UAE_Doctor_Clinic_Leads_Batch1.xlsx", "Batch 1")
    print(len(ROWS))
