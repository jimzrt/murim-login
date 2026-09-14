<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0377.txt",
      "sha256": "aad748ef4ca121770de119ed545653b02c71c68db95dc06441a35780183f3036",
      "bytes": 16906
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1a4166fc98adb0fd9bbd839dfe19b3b9712cb12ba8e9eaecc8f007cb2e02ab62",
      "bytes": 5136
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e537fb0d951bd079e045abf975e2219dc3b476a6a787b16b36f2f4df957d8584",
      "bytes": 6036
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "7f416fa89c7d5d4f7f98dcc4b648ddfcc57acf89b00dbed63f25a2dc606332b6",
      "bytes": 502
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "77591eeddb3911af5a9a9a9515e0ff5c2a77b95bcd9616b4fb1c83b35acbe412",
      "bytes": 5011
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "80aba61cc6604af9ac2f1b78ea226bb41ccd7fa2e870e317cef739a8853fd3a4",
      "bytes": 23777
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "ec3804d469a028185e18746fda70738c995b682321cce38824c22e444660a415",
      "bytes": 694
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b569919f9c23598d86efe26f2acec7ee3377f801e2a96869ba8039f97f8e29ca",
      "bytes": 4023
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 14398
}
-->

# Durable State Update — Chapter 377

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 377. Keep at most
2 continuity_sources. Use only chapter
numbers through 377. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.

Return this exact shape:

{
  "chapter": 377,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 377,
    "continuity_sources": [377],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.

## Prior durable context

```json
{
  "active_continuity": [
    "By the end of the source-only bridge, Jin Taekyung had reached the Supreme Peak realm and Level 120; this chapter grants him another level up, but the resulting level, exact current Fame, Titles, martial-art stages, and unassigned points are not stated.",
    "Jin Mukyung is Taekyung's second older brother, twenty-three, the Heaven Shaking Sword, a Peak-level martial genius, and substantially stronger than Taekyung.",
    "Dark Heaven rescued the former conspirators from the Demonic Cult, implanted gu in them, and its larger purpose and reason for sparing Taekyung remain unresolved.",
    "The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by the recent Dark Heaven attacks; Tang Sadok has awakened and is again serving as Family Head of the Sichuan Tang Clan.",
    "Tang Sadok confessed that he revealed the Myriad Poison Ring's location to the Western Heaven Demon Lord to preserve the Tang Clan; Taekyung forgave him, and the Tang Clan owes Taekyung's group a great debt.",
    "Taekyung completed the Hidden Quest Atonement and Forgiveness and acquired the Benefactor of the Tang Clan Title, along with EXP, Fame, and a level up.",
    "The Myriad Poison Ring was transferred to Taekyung by Tang Sadok and is now bound to him; White Flame, Myriad Poison Ring, and one still-unnamed item are currently bound.",
    "Mungyeong is the Divine Physician and the Slaughter Saint. He has left the Murim's affairs behind, intends to live as a physician, and is the master of Dongbong.",
    "Dongbong is Mungyeong's longtime disciple and a physician who lost his wife and two children to an epidemic before Mungyeong cured him and accepted him as a disciple.",
    "A hidden, currently inactive transport formation associated with Dark Heaven was found near Sichuan; its origin and function remain unresolved.",
    "Jin Wikyung has proposed relocating the Sichuan Tang Clan and has been assigned to escort Samgoe toward Henan.",
    "Taekyung's return to his original world is imminent, with roughly six hours having passed there.",
    "Cheongpung is Mimi's temporary guardian while the Tang Clan's future is uncertain.",
    "The Divine Physician, referred to in Taekyung's joke as Dongbong, has asked Taekyung for time before his departure; the request remains undisclosed.",
    "Dongbong predicts that a great war will soon occur and asks Mungyeong to prevent it as the Divine Physician; Mungyeong verbally refuses and says the Murim is not where he belongs, while the announced departure from Chengdu's western port remains unresolved.",
    "Taekyung and Cheongpung are preparing to leave Sichuan by fast ship from Chengdu's western port after the Hour of the Dog.",
    "Mu Song is the boatman associated with the water bandits preparing the ship.",
    "An unidentified boy reaches the port immediately before departure and is accepted as one more passenger."
  ],
  "continuity_sources": [
    376
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved in the accepted local anchor.",
    "Dark Heaven's agents, purpose, and connection to the transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination remain unresolved.",
    "The outcome and timing of the planned Samgoe escort to Henan remain unresolved.",
    "The identity and name of the third bound item remain unresolved.",
    "The matter the Divine Physician wants to discuss with Taekyung before his departure remains unresolved.",
    "The identity of the boy who arrives at the port and whether he will accompany Taekyung's group remain unresolved.",
    "Whether Mungyeong will ultimately intervene in the coming war or leave the Murim remains unresolved."
  ],
  "safe_through": 376,
  "temporary_decisions": [
    "This expedition deliberately skips accepted translation of Chapters 65–370.",
    "Chapters 371–373 are source-only bridge summaries and must not be treated as complete English continuity.",
    "When bridge context conflicts with the current Korean source, preserve the current source and record the uncertainty.",
    "Use Reformation Fist for 갱생권, grappling technique for 금나수, and retain hyung for 형 where the accepted anchor requires them.",
    "Render 반 시진 and 한 시진 as half a shichen and one shichen, with a footnote explaining that a shichen is a traditional two-hour period.",
    "Render 종형 as older cousin in this chapter's family context.",
    "Render 사죄와 용서 as Atonement and Forgiveness, 당문의 은인 as Benefactor of the Tang Clan, 백염 as White Flame, 동봉 as Dongbong, and 신의 as Divine Physician.",
    "Render 인산인해 as “a sea of people.”",
    "Render 홍무 as Hongwu and 성도 as Chengdu.",
    "Render 술시 as the Hour of the Dog, with a footnote identifying it as a traditional period roughly corresponding to 7–9 p.m.",
    "Render 선화아 as boatman and 무송 as Mu Song.",
    "Retain Master for 스승님 and render 살귀 as slaughter demon in Mungyeong's self-description."
  ],
  "version": 1
}
```

## Expedition bridge dossier

# Expedition Seed Dossier

This dossier is intentionally conservative. It orients the Chapter 370 catch-up.
It is not a substitute for translating Chapters 66–369, and it must not leak
plot from parked Chapters 371–375.

## Hard boundary

- Accepted English continuity is reliable through Chapter 65.
- Chapters 66–369 are skipped and have no accepted local English in this
  expedition.
- Chapter 370 is the next chapter to translate. Its Korean source is the
  authority for every beat in that chapter.
- Parked accepted translations of Chapters 374–375 exist in this branch. Do not
  read them, their reviews, or old 371–373 bridge summaries while drafting
  370–373.
- When the Korean source of the current chapter conflicts with this dossier or
  with Chapter 65 continuity, the current source wins. Do not invent missing
  backstory; preserve ambiguity and flag an unresolved continuity issue.

## Opening position for Chapter 370

Chapter 370's source opens at the Sichuan Tang Clan. About seven days have
passed since the Three-Sect Bloodbath. The clan's gates, long closed, are open
to reconstruction and to orthodox guests. Do not assert later names, ranks,
quests, or outcomes that the current chapter has not yet shown.

## Translation guardrails

- Treat the Korean source as authoritative for every line of the chapter being
  translated.
- Do not back-project titles, names, ranks, or skills from parked later
  chapters or web searches into the skipped range without current-source
  evidence.
- Use established local terminology where it exists from Chapters 0–65.
- For terms first evidenced in the current source, follow the ledger and
  first-use rules. Record new bindings through the normal update stage.
- The light, self-mocking first-person voice and the source's jokes remain
  important, but missing continuity must never be filled by invented exposition.

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 독룡각 | **Poison Dragon Pavilion** | Pavilion led by Tang Horyong |
| 당호룡 | **Tang Horyong** | Acting Family Head of the Sichuan Tang Clan |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 경천신니 | **Heaven-Shaking Divine Nun** | Murder victim named alongside Tang Sadok |
| 삼문혈사 | **Three-Sect Bloodbath** | Recent attack on three major orthodox sects |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 구파일방 | **Nine Sects and One Gang** | Major orthodox organizations |
| 오대세가 | **Five Great Families** | Major orthodox families |
| 소림혈사 | **Shaolin Bloodbath** | Earlier attack that galvanized orthodox Murim |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 만독지환 | **Myriad Poison Ring** | Item Taekyung considers taking before departure |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 동봉 | **Dongbong** | Name or designation associated with the Divine Physician. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |
| 사죄와 용서 | **Atonement and Forgiveness** | Hidden Quest completed by Taekyung. |
| 당문의 은인 | **Benefactor of the Tang Clan** | Title acquired by Taekyung. |
| 아미파 | **Emei Sect** | Orthodox sect whose nuns conduct the funeral rites. |
| 청성파 | **Qingcheng Sect** | Orthodox sect represented among the assisting martial artists. |
| 개방 | **Beggars' Sect** | Organization represented by the attending beggars. |
| 묘령사태 | **Satae Myo Ryeong** | Middle-aged Emei nun overseeing the funeral prayers. |
| 명진 | **Myeongjin** | Daoist assisting with the funeral rites. |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 후개 | **Future Beggar Chief** | Title used for Gung Gibang. |
| 기련삼괴 | **Qilian Samgoe** | The trio of monsters that includes Samgoe and Ilgoe. |
| 일괴 | **Ilgoe** | The strongest of the Qilian Samgoe, defeated single-handedly by Jin Taekyung. |
| 칠선자 | **Chilseonja** | Mysterious martial artist who blocked Samgoe's attack and saved Hyuk Mujin. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 화산신룡 | **Huashan Divine Dragon** | Epithet used for Jin Taekyung. |
| 열화신룡 | **Blazing Fire Divine Dragon** | New epithet acquired by Jin Taekyung. |
| 청풍고검 | **Clear Wind Ancient Sword** | Sect Leader of the Qingcheng Sect; epithet of the old Daoist. |
| 멸절신니 | **Extinction Divine Nun** | New Sect Leader of the Emei Sect after the death of the Heaven-Shaking Divine Nun. |
| 천주 | **Heavenly Lord** | Being worshiped as a god by Dark Heaven's fanatics. |
| 혈주 | **Blood Lord** | Dark Heaven figure whose power and abilities are recalled by Jin Taekyung. |
| 열화동 | **Blazing Fire Cave** | Cave at Mount Jiuhua containing an advanced arcane formation. |
| 진성애 | **Jin Seong-ae** | Jin Taekyung's joking title for himself as a sex-education teacher. |
| 구성애 | **Gu Seong-ae** | Real-world sex-education teacher referenced in Jin Taekyung's joke. |
| 삼도천 계곡 | **Valley of the Sanzu River** | Valley named after the Buddhist river separating the living world from the afterlife. |
| 노군백 | **No Gunbaek** | Level 170 opponent named in a System defeat message. |
| 귀염미 | **Gwiyeommi** | Pen name of a romance novelist. |
| 홍무 | **Hongwu** | Era name beginning when the civil war ends and a new emperor ascends. |
| 성도 | **Chengdu** | City whose western port is the departure point. |
| 선화아 | **boatman** | Nautical title used for Mu Song. |
| 무송 | **Mu Song** | Bronze-skinned boatman associated with the water bandits. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 혁무진 | 궁기방 | orthodox_ally_to_orthodox_ally | Young Hero Gung | blunt-but-formal | Uses 궁 소협 while teasing Gung Gibang about his injuries. |
| 혁무진 | 청풍 | junior_ally_to_younger_ally | Young Hero Cheong | formal-but-bewildered | Uses 청 소협 when reacting to Cheongpung's warning. |
| 혁무진 | 진태경 | subordinate_to_squad_leader | Squad Leader | deferential | Calls Taekyung 조장님 when announcing his awakening. |
| 궁기방 | 진태경 | squadmate_to_squad_leader | Jin Taekyung | familiar-but-direct | Calls Taekyung by name when he wakes. |
| 진태경 | 청풍고검 | junior_to_elder_sect_leader | Perfected One | respectful-formal | Uses 진인 when greeting the Qingcheng Sect Leader. |
| 청풍고검 | 진태경 | elder_sect_leader_to_junior_ally | Fellow Daoist Jin | respectful-but-familiar | Uses 진 도우 when greeting Taekyung. |
| 멸절신니 | 진태경 | elder_sect_leader_to_benefactor | Benefactor Jin | respectful-formal | Uses 진 시주 when greeting Taekyung. |
| 멸절신니 | 적천강 | orthodox_elder_to_orthodox_elder | Benefactor Jeok | respectful-but-familiar | Uses 시주 when responding to Jeok Cheongang. |
| 진태경 | 적천강 | disciple_to_elder_master | Old Man | casual-but-affectionate | Uses 노야 while thanking Jeok Cheongang. |
| 적천강 | 문경 | orthodox_elder_to_younger_orthodox_elder | Wen | hostile-but-blunt | Jeok Cheongang addresses Mungyeong as 문가 while intervening on Taekyung's behalf. |
| 진태경 | 문경 | ally_to_secret_identity_holder | Mungyeong | casual-but-teasing | Taekyung accepts the requested name and deliberately uses it in a familiar vocative. |
| 동봉 | 문경 | disciple_to_master | Master | deferential | Dongbong repeatedly addresses Mungyeong as 스승님 after affirming his identity as the Divine Physician. |
| 무송 | 진태경 | older_ally_to_junior_ally | junior | deferential-but-uncertain | Mu Song switches from junior to Young Hero Jin and Great Hero before Taekyung tells him to use junior. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 장강수로맹  | **Yangtze River Channel League** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 로그아웃             | **Logout**                     |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 성도 | **Chengdu** | City whose western port is the departure point. |

## Listed compact profiles

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 376
- **Aliases:** Future Beggar Chief
- **Role:** Young beggar and Future Beggar Chief; ally and squadmate of Jin Taekyung
- **Personality:** Sardonic, competitive, pragmatic, and willing to trade vicious banter with Hyuk Mujin
- **Voice:** Weary, blunt, informal, and sarcastic
- **Relationships:** Ally and squadmate of Jin Taekyung; frequent bickering companion of Hyuk Mujin

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 376
- **Aliases:** None revealed
- **Role:** Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 376
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 376
- **Aliases:** Slaughter Saint
- **Role:** Divine Physician and Slaughter Saint; master of Dongbong and physician caring for patients outside the Murim
- **Personality:** Regarded as unusually skilled for his age; dry, rigid, emotionally restrained, and blunt in his interactions
- **Voice:** Dry, blunt, and impassive as the Slaughter Saint; his Mungyeong persona is usually cheerful and convincing, though it becomes slightly darker after he resumes it.
- **Relationships:** Master of Dongbong; physician responsible for Jin Taekyung's recovery and caregiver to patients

## Korean source

```text
＃377화



“그들은, 떠났나?”

살이 토실토실하게 오른 중년인, 사천성주의 긴장 어린 물음에 호위장이 대답했다.

“예. 한 식경 전에 그들이 탄 장강수로맹의 쾌조선이 출항했습니다.”

“휴우우.”

뱃살이 출렁일 만큼 깊은 안도의 한숨을 내쉰 사천성주가 손을 내저었다.

“알겠으니 이만 물러가게. 혹시 무림인들에 관련된 소식이 있다면 바로바로 보고하고.”

“알겠습니다. 한데 성도 인근에 주둔시켜 놓은 병력은…….”

사천성주가 눈살을 찌푸렸다.

“이봐, 호위장.”

“예?”

“내가 그런 시시콜콜한 부분까지 신경 써야 하나? 그 정도 뒤처리는 자네들끼리 처리하라고. 도지휘사(都指揮使), 그 꼬장꼬장한 작자와 잘 상의를 하든가 해서. 응?”

“…….”

호위장은 내심 어이가 없었다.

이게 말인가 방귀인가. 성주의 무능함과 아랫사람에게 일 떠넘기는 버릇이야 하루 이틀 일이 아니지만 이건 해도 해도 너무했다.

‘아무리 그래도 이 정도는 아니었던 것 같은데.’

어느 날부터 애첩 하나를 들이더니 벌써 수년째 여색에 빠져 공무는 뒷전이다.

내심 한숨을 푹 내쉰 호위장이 힘없이 군례를 취했다.

“……성주님의 명을 받들겠습니다.”

“당연히 그래야지. 그럼 수고하라고. 난 바쁜 용무가 있어서 이만.”

그제야 만족스럽게 고개를 끄덕인 사천성주가 자리에서 일어났다.

과도한 체중 탓에 가쁜 숨을 내쉬며 멀어지는 그의 뒷모습을 바라보던 호위장이 개미만 한 목소리로 중얼거렸다.

“바쁜 용무는 무슨. 또 애첩이나 안으러 가겠지.”

호위장의 예상은 적중했다. 대전을 떠난 사천성주가 가장 먼저 찾은 곳은 바로 화려하게 치장된 침소였다.

“애향아! 애향아!”

어지간한 방보다 큰 비단 침상 위, 반나체로 누워 있던 미녀가 몸을 일으켰다.

“가가(哥哥). 왜 이제야 오셨어요? 애향이가 얼마나 기다렸는데.”

“그, 그랬느냐?”

새치름한 눈매에 한 번, 이불 사이로 슬쩍슬쩍 보이는 새하얀 살결에 두 번 넋이 나간 사천성주의 입이 헤벌쭉 벌어졌다.

“미안하구나. 호위장이 귀찮게 구는 바람에.”

“또 그 사람이에요? 안 그래도 가가께서 얼마나 바쁘신데 왜 그리 못살게 군대요?”

“그러게나 말이다.”

“이래서 무능력한 아랫것들이 문제예요. 가가께서 없으시면 다들 아무것도 못 하잖아요?”

“역시, 이 가가를 생각해 주는 건 우리 애향이밖에 없다!”

호위장이 들었으면 눈을 까뒤집었을 대화였다.

감동으로 볼살을 부르르 떠는 사천성주를 향해 애첩이 두 팔을 벌렸다.

“이리 오세요, 가가. 고생하셨으니까 이 애향이가 꼭 안아 드릴게요.”

“애향아……!”

사랑하는 애첩의 끈적하고도 고혹적인 눈웃음에, 사천성주의 눈동자가 몽롱하게 풀어졌다.

“세상 천하에 너처럼 아름다운 여인이 있을 수 있단 말이냐!”

삼공(三公)을 배출한 세도가의 핏줄로 태어나 탄탄대로를 걸어온 사천성주다.

마르지 않는 재물을 바탕으로 숱하게 기방을 들락거리며 온갖 미녀들을 품에 안았다.

마음이 혹하면 첩으로 들인 것도 수차례, 그러나 워낙 많은 여인을 만난 탓에 한 해를 버티지 못하고 시들해지고는 했다.

‘하지만 이 아이는 달라!’

맹세코 이런 여인은 처음 보았다. 목소리와 눈빛, 손끝 하나의 움직임까지. 사천성주의 눈에는 애향이의 모든 것이 매혹적이고 사랑스러웠다.

벌써 수년째 보아 온 모습이지만 도무지 질리지 않는다. 아니, 오히려 무서울 만큼 깊숙이 빠져들고 있었다.

“사랑한다. 사랑한다, 애향아!”

막 오십 줄에 접어든 사천성주의 외침은 사랑에 빠진 젊은이의 그것처럼 절절했다.

홀린 듯이 다가가 애첩의 품에 안긴 그는 언제나 그래 왔듯 오늘 하루 있었던 일을 말하기 시작했다. 사천성주에게 있어 애첩은 가장 은밀한 비밀까지 털어놓을 수 있는 유일한 사람이었다.

“……해서, 드디어 그 골칫덩이 무뢰배들이 떠났다.”

“무뢰배들이라면, 그들을 말씀하시는 거죠? 지난번에 찾아왔던 무림인들.”

“그래. 상산왕 전하의 증표를 가져왔던 그자들 말이다.”

“흐음.”

“왜 그러느냐?”

“아니에요, 아무것도. 그나저나 이번 일로 가가께서 고생 많으셨겠다. 들어 보니 무림인들끼리 시비가 붙어서 많은 사람이 죽고 다쳤다면서요?”

사천성주가 질린 얼굴로 고개를 내저었다.

“말도 말거라. 어디서 구했는지 감히 관군의 복식까지 훔쳐 입고 대국의 질서를 어지럽히다니.”

“어머, 정말요?”

“믿기지 않겠지만 사실이다. 내 다른 건 몰라도 그에 관해서는 반드시 조정에 장계를…….”

“어쩜 이리 대장부 같으실까. 그런데 가가.”

싱긋 웃은 애첩이 무릎에 얹힌 사천성주의 머리를 쓰다듬었다.

“황실에서 알게 된다면 일이 커지지 않을까요?”

“으, 응?”

“그렇잖아요. 언젠가는 가가께서도 삼공(三公)의 지위에 올라 문무백관을 거느리며 황상을 보필하실 텐데…… 소첩은 가가를 시기하는 무리가 이번 일을 문제 삼지는 않을까 걱정이 되어요.”

“허허. 역시 날 이만큼 생각해 주는 것은 애향이, 너밖에 없구나.”

사천성주는 애정이 뚝뚝 묻어나는 눈빛으로 자신의 애첩을 바라보았다.

그러나 그 역시 아주 얼간이는 아니었다.

비록 관과 무림이 서로를 소 닭 보듯 하는 상호 불가침의 영역이라고는 하지만, 지난 칠 주야 동안 천 명이 훌쩍 넘는 사람들이 사천 땅 곳곳에서 죽어 나갔다.

자질구레한 뒤처리는 아랫놈들에게 떠넘기더라도 최소한 이것만큼은 직접 나서야 한다.

“네 마음씨가 갸륵하나, 지금처럼 큰 사안은 오히려 숨길수록 문제가 되기 마련이다.”

“가가도 참. 제가 그걸 모를 것 같아요?”

“음? 그럼 어쩌자는 것이냐?”

“숨길 건 숨기고, 공은 부풀려야죠.”

교태 가득한 목소리가 사천성주의 귓가를 간지럽혔다.

“무림인들 간에 큰 분쟁이 있었고, 가가께서 휘하의 관군을 움직여 이 사태를 진정시킨 것으로.”

“으음.”

“가가께서는 무뢰배들의 손에 어지럽혀진 대국의 질서를 바로 세우고, 민초들을 보살핀 어진 성주가 되시는 거예요. 물론 관의 무기와 의복에 관한 이야기는 빼놓는 게 좋겠죠? 오해를 살 수도 있으니까.”

“애향이 네 말대로만 된다면 좋겠지만. 아무리 그래도 장계를 거짓으로 꾸며 올리기에는 좀…….”

“가가, 절 보세요.”

머뭇거리던 사천성주는 흑요석처럼 아름답게 반짝거리는 눈동자를 보고 외마디 탄성을 흘렸다.

“아.”

“이 애향이를, 가가를 사모하는 제 뜻을 모르시나요?”

“그것이, 그러니까…….”

사천성주는 말을 잇지 못했다.

애첩과 눈이 마주친 순간, 이미 머릿속은 텅 비워진 지 오래였다.

고혹적인 자태에 가슴이 떨리고 꽃향기 같은 채취에 정신이 아득해진다.

어디에선가 불쑥 솟구친 무한한 신뢰와 애정, 그리고 참을 수 없는 욕망이 그를 지배했다.

“애향아, 애향아!”

간절한 목소리. 하지만 애첩은 자신의 몸을 더듬어 오는 사천성주의 손길을 붙잡았다.

“가가, 대답은요?”

“다, 당연히 네 뜻에 따르마. 너를 위해서라면 내 무엇이든 하겠다!”

애첩의 입가에 맺힌 웃음이 짙어졌다.

“잘하셨어요. 지금까지 그랬던 것처럼, 앞으로도 그렇게 하시면 되는 거예요. 아셨지요?”

“응, 응!”

강렬한 욕망에 사로잡힌 사천성주는 미처 볼 수 없었다.

자신이 그토록 사랑하는 애첩의 눈동자에 요사스러운 붉은빛이 스며드는 불길한 광경을.

“아이, 착해라. 우리 성주님. 말도 잘 듣네.”

애첩은 소리 내어 깔깔 웃었다.

모든 것은 그녀가, 아니 그분이 원하는 방향으로 흘러가고 있었다.



* * *



“음?”

“왜 그러세요?”

“아니, 방금 무슨 미친년 웃는 소리를 들은 것 같아서.”

“미친년이요? 여기서요?”

“응. 쎄하더라고.”

나와 혁무진은 주위를 둘러봤다. 드넓은 장강의 지류, 수룡채의 깃발을 내건 세 척의 쾌조선은 막힘없이 나아가고 있었고 당연하지만 그중 어디에도 여인은 없었다.

“잘못 들었나? 이상하네.”

요새 온갖 일을 다 겪었더니 이제 환청이 다 들리나.

고민하는 내게 혁무진이 심각한 얼굴로 입을 열었다.

“혹시 그…….”

“그, 뭐?”

“앞줄 우측 네 번째에 서 있던 소저를 잊지 못하신 것 아닙니까?”

궁기방이 고개를 저었다.

“헛소리. 좌측 세 번째야. 그 정도면 잊지 못할 미모지.”

“아, 뭔가 했더니 그 이야기였어?”

나는 인자하게 웃으며 두 녀석을 바라보았다.

“내 생각에는, 오늘이 너희 둘한테 잊지 못할 하루가 될 것 같은데.”

환히 웃는 얼굴로 손짓하자 그걸 보고 달려온 건장한 수적 여럿이 굽신굽신 고개를 조아렸다.

“부르셨습니까요, 진 대협.”

“혹시 쇤네들에게 뭐 시키실 일이라도.”

“저 새끼들 붙잡아서 장강에 찍먹 해 주세요.”

수적들이 어리둥절한 얼굴로 되물었다.

“어, 찍먹이라 하셨습니까?”

“죄송하지만 저희가 원체 무식한 놈들이라. 당최 찍먹이 무엇입니까?”

“찍먹은 올바른 문화……가 아니라, 그냥 제가 멈추라고 할 때까지 계속 머리통만 담갔다가 빼 주시면 됩니다.”

“아아, 예.”

“쉽구먼요.”

“자, 잠깐만!”

“조장님!”

궁기방과 혁무진은 저항하려 했지만 턱도 없는 일이었다.

한 놈은 다리 한 짝만 멀쩡하고, 다른 한 놈은 전신이 붕대로 감겨 있었으니까.

무공을 익힌 건장한 떡대들이 우르르 몰려와 사지를 붙들고 찍먹쇼를 시작하는 사이, 나는 앞서 허공에 띄워 둔 시스템창을 바라봤다.



- 아직 이름을 정하지 않은 종속 아이템이 있습니다. 확인하시겠습니까?



‘당연히 예스.’

띠링.



아이템창



[???]

종류 : 방어구

등급 : 신병이기

제한 : 진태경

설명 : 이름 모를 고대 야장의 혼이 깃든 갑옷. 실로 가공할 만한 방어력을 지녔으며, 현재는 전 주인이 사망함으로써 새로운 주인에게 소유권이 종속되었다. 이름을 지어 주면 어디에서나 자유롭게 사용할 수 있다.





‘전 주인이 사망해서 소유권이 종속되었다고?’

설마 했는데, 내가 생각하는 그 물건이 맞는 것 같다.

나는 인벤토리를 탈탈 털어 본 끝에 새로운 종속 아이템을 확인할 수 있었다. 그리고 저절로 흘러나오는 김빠진 소리.

“……에게?”

손바닥 위에 올려진 그것은 자그마한 파편에 불과했다. 본래는 흑룡갑(黑龍鉀)이라 불리던 물건이기도 했다.

‘분명히 마지막에 일섬으로 서천마군, 그놈과 함께 날려 버렸는데. 종속 아이템이라 인벤토리에 자동으로 들어온 건가.’

흑룡갑이 산산조각 나던 광경이 아직도 눈앞에 선하다.

그런데 겨우 이만한 파편으로 뭘 어떻게 하라는 건지 모르겠네.

‘팬티 앞부분에 넣어 두면 세상 든든하긴 할 것 같은데.’

아, 혹시 이래서 방어구인 건가.

슬쩍 바지 앞섬을 잡아당겨 적절한 위치를 살피던 그때였다.

“거기서 뭐 하…….”

“……아.”

순간 내려앉은 싸늘한 침묵.

풀어진 바지춤과 그 안에 쑥 들어간 내 손을 본 소년의 얼굴이 딱딱하게 굳는다.

주위에 아무도 없는 것을 확인한 쌀성, 아니 문경이 입을 열었다.

“이걸 하필, 여기서?”

“아니, 잠깐만. 이거 오해가 좀 있는 것 같은데요.”

내가 황급히 변명하려던 찰나, 문경의 눈빛이 착 가라앉았다.

“출발할 때 말했을 텐데. 화왕과 청풍을 제외한 다른 사람 앞에서는 문경으로 대하라고.”

나는 억울한 얼굴로 대답했다.

“너도 지금 반말하고 있잖아, 새꺄.”

“……!”

“아, 죄송.”

만감이 교차하는 표정을 짓던 문경이 근처로 다가온 수적들을 곁눈질하며 혀를 찼다.

무시무시한 살성이 신의의 제자이자 밝은 소년 의생의 모습으로 변하는 것은 순식간이었다.

“뭐 하고 계셨어요?”

“네가 알아서 뭐 하게.”

“……!”

이거 은근히 재밌네. 그런데 세 번은 못 하겠다.

나는 말문이 막힌 문경을 향해 얼른 손을 내밀었다.

“이게 바지춤에 들어가서.”

물론 사실과는 살짝 괴리감이 있지만, 문경은 그런 것 따위는 신경 쓰지 않았다. 정확히 말하자면, 흑룡갑의 파편에 시선이 고정되어 있었다.

“이건…….”

“혹시 아시는 물건. 아니, 아는 물건이냐?”

“어디서 얻었습니까?”

“그놈에게서.”

서천마군을 뜻한다는 것을 알아들은 문경이 고개를 끄덕였다.

“신병이기(神兵利器)를 얻으셨군요. 어쩌다가 파편만 남았는지는 모르겠지만.”

“놈은 이걸 흑룡갑이라고 부르던데.”

“흑룡갑?”

“왜, 알고 있던 이름이랑 달라?”

“오래된 비사(祕史)에서 읽은 적이 있습니다. 정해진 이름이 없으며, 소유자에 따라 형태와 성질이 바뀐다는 신비한 갑옷에 대한 이야기를.”

“형태와 성질이 바뀐다고? 어떻게?”

문경은 한심하다는 눈빛으로 대답을 대신했다. 그리고 나는 그제야 지금부터 무엇을 해야 할지 깨달았다.

‘공력.’

공력이야말로 소유자가 지닌 형태와 성질, 그 자체다.

스아아아.

팔 성에 오른 열화신공의 구결에 따라 용암 같은 기운을 흑룡갑의 파편을 향해 흘려보냈다.

파편의 표면에 감돌던 묵색 기운이 사라지고, 빈자리를 청백색의 열양지기가 채웠다.

불꽃이 이글거리는 듯한 문양이 새겨진 그것은, 더 이상 흑룡갑이라 부를 수 없는 물건이었다.

‘화룡갑(火龍鉀).’

단순하지만 이보다 적절한 이름은 존재하지 않을 것이다.

내가 만족스러운 미소를 머금음과 동시에 경쾌한 종소리가 울려 퍼졌다.

띠링.



- 당신은 종속 아이템, [???]에게 새로운 이름을 부여했습니다!

- 지금부터 [화룡갑]을 어디에서나 자유롭게 사용할 수 있습니다!

- [화룡갑]이 당신의 기운과 공명합니다! 스스로 파손 부위를 복구하기 위해 소유자의 힘을 원합니다!



쏴아악.

느껴진다. 체내로부터 빠져나간 막대한 공력이 화룡갑을 향해 몰려드는 것이.

나는 스펀지처럼 공력을 빨아들인 그것을 품에 넣는 척, 인벤토리에 수납했다.

‘자동 복구라, 끝내주는데.’

확실히 쓸모있는 물건을 얻었다.

다행이다. 이번 여정에서 얻은 마지막 선물이 화룡갑이라서.

돌아서려는 나를, 문경이 눈을 크게 뜨고 바라봤다.

“어딜 가느, 가십니까?”

“네가 알아서 뭐 하게.”

“……!”

아, 이거 어쩐지 중독 될 것 같아.

나는 속으로 ‘참을 인’ 자를 되새기고 있을 문경에게 손을 흔들어 주었다.

“한숨 자러 간다. 깨우지마라.”

“……?”

그래, 이제는 오랜 잠에서 깨어날 때다.

그런데…….

‘왜 이렇게 찝찝하지? 뭘 잊었나?’

갸웃거리며 쾌조선의 선실에 자리를 잡고 누운 나는 눈을 감았다. 깊이 심호흡하며 명령어를 외쳤다.

‘로그아웃.’

띠링.



- 10초 후 로그아웃합니다. 십, 구, 팔, 칠…….



마지막 카운트와 함께, 어디선가 물장구 소리와 누군가의 외침이 아련하게 귓가를 파고들었다.

첨벙, 푸하! 조장님, 살려, 푸하!
```

## Final English reading copy

```markdown
# Chapter 377

“They’ve left?”

The guard captain answered the tense question from the plump middle-aged Sichuan Governor.

“Yes. The fast ship belonging to the Yangtze River Channel League departed one sikgyeong ago.[^1]”

“Pheeeeew.”

The Sichuan Governor let out a deep sigh of relief, his belly wobbling, and waved a hand.

“All right, you may withdraw. If you hear anything related to the martial artists, report it to me immediately.”

“Understood. But the troops stationed near Chengdu…”

The Sichuan Governor frowned.

“Listen, Guard Captain.”

“Yes?”

“Do I have to concern myself with every little detail? Handle that kind of cleanup among yourselves. Consult the Provincial Military Commissioner—that stubborn bastard—if you have to. Hmm?”

“…”

The Guard Captain was speechless inside.

*Was that supposed to be an order or a fart?*

The governor’s incompetence and habit of dumping work on his subordinates were nothing new, but this was too much even for him.

*Even so, I don’t remember him being this bad.*

Several years ago, he had taken a favorite concubine, and ever since then, he had been so consumed by women that official duties had become an afterthought.

The Guard Captain sighed inwardly and weakly performed a military salute.

“…I will carry out Your Excellency’s order.”

“Of course you will. Then get to work. I have an urgent matter to attend to, so I’ll be going.”

Only then did the Sichuan Governor nod with satisfaction and rise from his seat.

The Guard Captain watched his back recede as he walked away, panting from his excessive weight. Then he muttered in a voice as tiny as an ant.

“Urgent matter, my ass. He’s just going to embrace his favorite concubine again.”

The Guard Captain’s prediction was accurate. The first place the Sichuan Governor visited after leaving the main hall was an extravagantly decorated bedroom.

“Ae-hyang! Ae-hyang!”

A beautiful woman lying half-naked on a silk bed larger than most rooms sat up.

“My dear. Why did you take so long? Ae-hyang has been waiting for you.”

“Y-You have?”

The Sichuan Governor was dazed once by her coy eyes and twice by the dazzling white skin that peeked out from between the blankets. His mouth fell open in a foolish grin.

“I’m sorry. The Guard Captain was bothering me.”

“That man again? You’re already so busy, my dear. Why does he keep giving you such a hard time?”

“Exactly.”

“That’s the problem with incompetent underlings. They can’t do anything without you, can they?”

“As expected, you’re the only one who truly cares about me, Ae-hyang!”

The Guard Captain would have rolled his eyes if he had heard the conversation.

The favorite concubine opened both arms toward the Sichuan Governor, whose cheeks trembled with emotion.

“Come here, my dear. You’ve worked so hard. Let Ae-hyang hold you.”

“Ae-hyang…”

At the sight of his beloved concubine’s sultry, alluring smile, the Sichuan Governor’s eyes grew hazy.

“Could there truly be a woman in all the world as beautiful as you?”

The Sichuan Governor had been born into a powerful family that had produced Grand Councilors, and his path through life had always been smooth.

Backed by inexhaustible wealth, he had frequented pleasure quarters and held countless beautiful women in his arms.

He had taken several of them as concubines whenever they caught his fancy. But because he had met so many women, he always lost interest before a year had passed.

*But this girl is different!*

He swore he had never seen a woman like her. Her voice, her eyes, even the smallest movement of her fingertips—everything about Ae-hyang was captivating and lovable in his eyes.

He had been seeing her for years, yet he had never grown tired of her. No—if anything, he was sinking deeper into her grasp, to a frightening degree.

“I love you. I love you, Ae-hyang!”

The Sichuan Governor was just entering his fifties, but his cry was as heartfelt as that of a young man who had fallen in love.

He approached her as if possessed and nestled into her arms. As he always did, he began telling her about everything that had happened that day. To the Sichuan Governor, his favorite concubine was the only person to whom he could reveal even his most private secrets.

“…And so, those troublesome rogue bastards finally left.”

“By rogues, you mean them, right? The martial artists who came here last time.”

“That’s right. The ones carrying His Highness the King of Shangshan’s token.”

“Hmm.”

“What is it?”

“Nothing. Anyway, you must have had a hard time because of this. I heard that the martial artists got into a dispute and many people were killed or injured.”

The Sichuan Governor shook his head with a disgusted expression.

“Don’t remind me. They dared to steal government uniforms and wear them, throwing the order of the empire into chaos.”

“Oh my, really?”

“It may be hard to believe, but it’s true. Whatever else I may overlook, I will certainly submit a memorial to the court about that…”

“How gallant of you. But, my dear…”

The concubine smiled sweetly and stroked the Sichuan Governor’s head where it rested on her lap.

“Wouldn’t it become a serious matter if the imperial court found out?”

“Huh?”

“Think about it. One day, you will rise to the position of a Grand Councilor, command all the civil and military officials, and assist His Majesty… I’m worried that the factions jealous of you might use this incident against you.”

“Ha ha. As expected, you’re the only one who cares about me this much.”

The Sichuan Governor gazed at his concubine with overflowing affection.

But he was not a complete fool.

Though the government and the Murim treated each other as they would a cow and a chicken, maintaining mutually inviolable spheres, more than a thousand people had died throughout Sichuan over the past seven days and nights.

He could dump the minor cleanup on his subordinates, but he needed to handle at least this much himself.

“Your concern is touching, but the more one tries to hide an important matter like this, the worse the problem becomes.”

“Oh, my dear. Do you think I don’t know that?”

“Hmm? Then what do you suggest?”

“Hide what needs to be hidden and exaggerate your achievements.”

Her coquettish voice tickled the Sichuan Governor’s ear.

“There was a major conflict among the martial artists, and you mobilized the government troops under your command to calm the situation.”

“Hmm…”

“You’ll become a wise governor who restored the empire’s order after it was thrown into chaos by a group of rogues and cared for the common people. Of course, it would be best to leave out anything about the government weapons and uniforms, don’t you think? They might cause a misunderstanding.”

“It would be nice if everything went as you said, Ae-hyang. But even so, submitting a false memorial feels a little…”

“My dear, look at me.”

The hesitating Sichuan Governor let out a short exclamation when he saw her eyes glittering beautifully like obsidian.

“Ah.”

“Don’t you understand Ae-hyang’s feelings? Don’t you understand how much I adore you?”

“I… I mean…”

The Sichuan Governor could not continue.

The moment his eyes met hers, his mind had already been emptied.

His heart trembled at her bewitching figure, and the floral scent of her body made his thoughts swim.

Boundless trust and affection that had surged up from somewhere, along with unbearable desire, seized control of him.

“Ae-hyang, Ae-hyang!”

His voice was desperate, but the concubine caught the Sichuan Governor’s hand as it wandered over her body.

“My dear, what is your answer?”

“O-Of course I’ll do as you wish. I would do anything for you!”

The smile at the corner of the concubine’s mouth deepened.

“Good. Just keep doing that, as you have until now. Understood?”

“Yes, yes!”

The Sichuan Governor, consumed by fierce desire, failed to notice.

A sinister red light had begun to seep into the eyes of the concubine he loved so dearly.

“Oh, what a good boy. Our governor listens so well.”

The concubine burst into loud laughter.

Everything was proceeding exactly as she—or rather, the one above her—desired.

* * *

“Hmm?”

“What’s wrong?”

“I thought I just heard some crazy bitch laughing.”

“A crazy bitch? Here?”

“Yeah. It gave me the creeps.”

Hyuk Mujin and I looked around. Three fast ships flying the flag of the Water Dragon Stronghold were gliding smoothly along the broad tributary of the Yangtze, and naturally, there wasn’t a woman anywhere among them.

“Did I hear wrong? That’s strange.”

*After everything I’ve been through lately, am I hallucinating now?*

As I pondered the matter, Hyuk Mujin spoke with a serious expression.

“Could it be that…”

“That what?”

“Perhaps you still cannot forget the young lady standing fourth from the right in the front row?”

Gung Gibang shook his head.

“Nonsense. It was the third from the left. Anyone would be unable to forget a beauty like that.”

“Oh, that’s what this was about?”

I smiled benevolently at the two of them.

“I think today is going to be an unforgettable day for you two.”

I waved them over with a bright smile. Several burly river bandits came running over and bowed repeatedly.

“Did you call for us, Great Hero Jin?”

“Is there something you want us humble men to do?”

“Grab those two bastards and give them a dip in the Yangtze.”

The river bandits looked bewildered.

“Uh, did you say a dip?”

“We’re ignorant fellows, you see. What exactly is ‘dip’?”

“Dipping is the civilized way… No, forget that. Just keep dunking their heads in and pulling them out until I tell you to stop.”

“Oh, yes.”

“Easy enough.”

“W-Wait!”

“Squad Leader!”

Gung Gibang and Hyuk Mujin tried to resist, but it was utterly futile.

One of them had only one good leg, while the other was wrapped in bandages from head to toe.

As a group of burly martial artists swarmed over, seized their limbs, and began the great dunking show, I looked at the System window I had already left floating in the air.

> **System**
>
> You have an unnamed bound item. Would you like to inspect it?

*Obviously, yes.*

A cheerful chime rang out.

> **System**
>
> **Item Window**
>
> **???**
>
> **Type:** Armor  
> **Grade:** Divine Weapon  
> **Restriction:** Jin Taekyung  
> **Description:** Armor imbued with the spirit of an unknown ancient blacksmith. It possesses truly formidable defensive power. With the death of its previous owner, ownership has become bound to a new owner. Once given a name, it can be used freely anywhere.

*Its ownership became bound because the previous owner died?*

I had suspected as much, but it seemed that this really was the object I thought it was.

After turning my inventory upside down, I finally found the new bound item. A flat, deflated sound escaped my lips.

“…Huh?”

The object resting on my palm was nothing more than a tiny fragment. It had originally been called Black Dragon Armor.

*I definitely blew it away with that bastard, the Western Heaven Demon Lord, in the final slash. Did it automatically enter my inventory because it was a bound item?*

The sight of the Black Dragon Armor shattering into pieces was still vivid before my eyes.

But I had no idea what I was supposed to do with a fragment this small.

*It would certainly make me feel secure if I tucked it into the front of my underwear.*

Ah. Maybe that was why it was classified as armor.

I was tugging at the front of my pants and inspecting a suitable position when—

“What are you doing th—”

“…Ah.”

A chilly silence descended in an instant.

The boy’s face stiffened when he saw my loosened waistband and the hand thrust inside it.

After making sure there was no one nearby, the Slaughter Saint—no, Mungyeong—spoke.

“Why here, of all places?”

“Wait a second. I think there’s been a misunderstanding.”

Just as I hurriedly began to make excuses, Mungyeong’s gaze turned cold.

“I told you when we departed. In front of anyone other than the Fire King and Cheongpung, you are to address me as Mungyeong.”

I answered with an aggrieved expression.

“You’re speaking casually to me right now too, you bastard.”

“…!”

“Oh. Sorry.”

Mungyeong wore an expression of conflicting emotions as he glanced sideways at the river bandits approaching nearby and clicked his tongue.

The terrifying Slaughter Saint transformed into the Divine Physician’s Disciple—a cheerful young physician-in-training—in an instant.

“What were you doing?”

“What business is it of yours?”

“…!”

*This is surprisingly fun. But I don’t think I can do it three times.*

I quickly held out my hand toward the speechless Mungyeong.

“This got into the front of my pants.”

That was slightly at odds with the truth, of course, but Mungyeong did not care about such details. More precisely, his eyes were fixed on the fragment of the Black Dragon Armor.

“This is…”

“Do you happen to know this? No—do you know it?”

“Where did you get it?”

“From that bastard.”

Mungyeong understood that I meant the Western Heaven Demon Lord and nodded.

“You obtained a divine weapon. Though I do not know how only a fragment remained.”

“He called it Black Dragon Armor.”

“Black Dragon Armor?”

“Why? Is that different from the name you knew?”

“I read about it in an old secret history. It was a mysterious armor with no fixed name, said to change its form and properties according to its owner.”

“It changes its form and properties? How?”

Mungyeong answered with a look that said I was hopeless. Only then did I realize what I needed to do next.

*Internal energy.*

Internal energy was the very form and nature possessed by its owner.

Whoooosh.

Following the formula of the Blazing Flame Divine Art, which had reached its eighth stage, I sent magma-like energy toward the fragment of the Black Dragon Armor.

The ink-dark energy swirling across the fragment’s surface disappeared, and bluish-white Scorching Yang Qi filled the empty space.

Engraved with patterns that seemed to writhe with blazing flames, it was no longer something that could be called Black Dragon Armor.

*Flame Dragon Armor.*

It was a simple name, but there could be no more suitable one.

At the same moment that I smiled with satisfaction, a bright chime rang out.

> **System**
>
> You have given the bound item ??? a new name!
>
> From now on, you can freely use Flame Dragon Armor anywhere!
>
> Flame Dragon Armor is resonating with your qi! It requires its owner’s power to repair its damaged sections by itself!

Whoosh.

I could feel it. A massive amount of internal energy was leaving my body and rushing toward the Flame Dragon Armor.

I pretended to tuck it into my robes and stored it in my inventory instead.

*Automatic repairs? That’s incredible.*

I had certainly obtained something useful.

*Thank goodness the final gift of this journey was the Flame Dragon Armor.*

As I turned away, Mungyeong stared at me with wide eyes.

“Where are you go—going?”

“What business is it of yours?”

“…!”

This was strangely addictive.

I waved at Mungyeong, who I knew was silently repeating the character for patience.

“I’m going to get some sleep. Don’t wake me.”

“…?”

Yes. It was time to wake from a long sleep.

But…

*Why do I feel so uneasy? Did I forget something?*

I tilted my head, then found a place in the cabin of the fast ship and lay down. I closed my eyes, took a deep breath, and called out the command.

*Logout.*

A chime rang out.

> **System**
>
> Logging out in 10 seconds. Ten, nine, eight, seven…

With the final count, the sound of splashing and someone’s cries faintly pierced my ears from somewhere.

Splash, gasp! Squad Leader, save me! Gasp!

[^1]: A sikgyeong was the time required to eat a meal, conventionally treated as roughly thirty minutes.
```
