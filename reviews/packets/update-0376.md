<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0376.txt",
      "sha256": "238732649bf11ec07be4eca4ea6ae273f76eedcf8ee82579ec8256b63ebca2e1",
      "bytes": 14344
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "61b2e7d06bf66e34871a3e4eab9284cd5c5a493b40741978a795f7495734b0f5",
      "bytes": 3726
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d8cf1c0e460989c0e90b87de42e2d975206887b901a5276c0e50d2ed473c1e17",
      "bytes": 5717
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "58a4b57338e116f2b1bfc884f3802cfd13c1e0c77e475f3701047d0e26f494ac",
      "bytes": 502
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2195e041f42ba3f1719a680dbc4d6b624716507da9f2666519eecc644c3ed031",
      "bytes": 5011
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bc3d7a9ddfb5153904fc171c73b3e0003a0e1509efc97a55e1dd9c4c1aaf6379",
      "bytes": 23777
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "2249038ea84d75c5163691534eb35ad067e2c316e53738503a4508deb5609012",
      "bytes": 8063
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "c0cae3aa9599405a58a738a883a36fc674ff9b7aae66f82100dd3d07bea88630",
      "bytes": 642
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3168bc6cf2a137b97dab148f677f41df7717343d602a30a0c35b11b557d9b862",
      "bytes": 3657
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 12795
}
-->

# Durable State Update — Chapter 376

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 376. Keep at most
2 continuity_sources. Use only chapter
numbers through 376. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 376,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 376,
    "continuity_sources": [376],
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
    "Slaughter Saint is concealing his identity as the young physician Mungyeong and intends to leave Murim after intervening in the recent crisis.",
    "A hidden, currently inactive transport formation associated with Dark Heaven was found near Sichuan; its origin and function remain unresolved.",
    "Jin Wikyung has proposed relocating the Sichuan Tang Clan and has been assigned to escort Samgoe toward Henan.",
    "Taekyung's return to his original world is imminent, with roughly six hours having passed there.",
    "Cheongpung is Mimi's temporary guardian while the Tang Clan's future is uncertain.",
    "The Divine Physician, referred to in Taekyung's joke as Dongbong, has asked Taekyung for time before his departure; the request remains undisclosed."
  ],
  "continuity_sources": [
    374,
    375
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved in the accepted local anchor.",
    "Dark Heaven's agents, purpose, and connection to the transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination remain unresolved.",
    "The outcome and timing of the planned Samgoe escort to Henan remain unresolved.",
    "The identity and name of the third bound item remain unresolved.",
    "The matter the Divine Physician wants to discuss with Taekyung before his departure remains unresolved."
  ],
  "safe_through": 375,
  "temporary_decisions": [
    "This expedition deliberately skips accepted translation of Chapters 65–370.",
    "Chapters 371–373 are source-only bridge summaries and must not be treated as complete English continuity.",
    "When bridge context conflicts with the current Korean source, preserve the current source and record the uncertainty.",
    "Use Reformation Fist for 갱생권, grappling technique for 금나수, and retain hyung for 형 where the accepted anchor requires them.",
    "Render 반 시진 and 한 시진 as half a shichen and one shichen, with a footnote explaining that a shichen is a traditional two-hour period.",
    "Render 종형 as older cousin in this chapter's family context.",
    "Render 사죄와 용서 as Atonement and Forgiveness, 당문의 은인 as Benefactor of the Tang Clan, 백염 as White Flame, 동봉 as Dongbong, and 신의 as Divine Physician."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 동봉 | **Dongbong** | Name or designation associated with the Divine Physician. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 화산신룡 | **Huashan Divine Dragon** | Epithet used for Jin Taekyung. |
| 열화신룡 | **Blazing Fire Divine Dragon** | New epithet acquired by Jin Taekyung. |

## Listed compact profiles

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 371
- **Aliases:** Future Beggar Chief
- **Role:** Young beggar and Future Beggar Chief; ally and squadmate of Jin Taekyung
- **Personality:** Sardonic, competitive, pragmatic, and willing to trade vicious banter with Hyuk Mujin
- **Voice:** Weary, blunt, informal, and sarcastic
- **Relationships:** Ally and squadmate of Jin Taekyung; frequent bickering companion of Hyuk Mujin

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 373
- **Aliases:** None revealed
- **Role:** Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 371
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 65
- **Aliases:** None revealed
- **Role:** Thirty-five-year-old Lesser Family Head of the Jin Family of Taiyuan
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 373
- **Aliases:** Slaughter Saint
- **Role:** Young Disciple of the Divine Physician overseeing Jin Taekyung's care
- **Personality:** Regarded as unusually skilled for his age; dry, rigid, emotionally restrained, and blunt in his interactions
- **Voice:** Dry, blunt, and impassive as the Slaughter Saint; his Mungyeong persona is usually cheerful and convincing, though it becomes slightly darker after he resumes it.
- **Relationships:** Disciple of the Divine Physician and physician responsible for Taekyung's recovery

## Korean source

```text
＃376화



인산인해(人山人海).

그렇게밖에 표현할 수 없는 광경이었다.

산서잠룡, 아니 열화신룡 진태경과 화산신룡 청풍이 떠난다는 소식을 들은 사람들이 구름처럼 모여들었기 때문이었다.

비단 무림인뿐만 아니라 겁 없는 양민들까지 더해지니, 배웅에 나선 인파는 꼬리에 꼬리를 물고 늘어져 셀 수가 없었다.

“잘 가시오! 열화신룡!”

“사천 무림은 그대들을 잊지 않을 거요!”

“뿔 달린 뱀이다! 화산신룡이 뿔 달린 뱀을 갖고 있다!”

“헉, 뱀이 공중제비를 돌았다!”

“화왕! 화왕이 뱀을 붙잡아서 태우려고 하고 있다!”

웅성거리는 소음이 행렬을 따라 서서히 멀어져 간다.

그리고 아무도 찾지 않는 언덕 위, 나무 그루터기에 앉아 모든 광경을 지켜보고 있던 소년이 문득 입을 열었다.

“멀리도 왔구나.”

“그러게 말입니다. 힘이 드는군요.”

거친 숨소리와 함께 풀밭에 털썩 주저앉는 늙은 제자의 모습에 소년, 문경은 중얼거렸다.

“……참으로 멀리도 왔어.”

거리를 말하는 것이 아니다. 지금 문경은 지나온 세월을 이야기하고 있었다.

“우리가 처음 만났던 때를 기억하느냐?”

“어찌 잊을 수 있겠습니까.”

늙은 제자는 이마에 맺힌 땀을 훔쳤다. 마치 그날의 따가운 햇볕이 자신에게 내리쬐고 있는 것처럼.

“홍무(洪武) 일 년. 유난히도 무더웠던 그해 여름을.”

황위를 둘러싼 내전이 끝나고 새로운 천자가 즉위한 해였다.

젊고 야심만만한 황제는 연호(年號)를 바꾸고 개혁을 꾀했으나, 기나긴 내전으로 피폐해진 백성들은 천자의 뜻을 받들어 개혁에 동참하기에는 너무나 지쳐 있었다.

“천하 각지에서 반란이 일어나고, 도적이 들끓었지.”

“가뭄이 들고 메뚜기 떼가 평야를 휩쓸었습니다. 관군과 반란군의 시신이 도처에 가득하니 역병이 창궐했지요.”

“그래, 실로 난세(亂世)였다.”

죽음은 또 다른 죽음을 낳았고 이내 대륙을 집어삼켰다.

동씨 성을 쓰는 젊은 목수 역시 천하에 드리워진 어두운 그림자를 피할 수는 없었다.

“지금도 가끔 그때를 생각하고는 합니다.”

수십 년의 세월이 바꿔 놓은 것은 강산뿐만이 아니다. 사랑하는 두 아이와 아내를 역병으로 잃어야 했던 젊은 목수는 어느덧 늙은 의원이 되어 있었다.

“제가 조금만 빨랐더라면, 더 빨리 스승님을 찾았다면 가족들을 살릴 수 있지 않았을까 하는 생각 말입니다.”

“후회하느냐?”

“예.”

하늘과 가까운 언덕에 앉아, 떠다니는 조각구름을 바라보는 늙은 의원의 눈동자는 어느새 젊은 목수의 그것으로 돌아가 있었다.

“이 숨이 붙어 있는 한 평생토록.”

고작 하루 차이였다.

목수가 역병에 걸린 몸을 이끌고 화전민촌에 머무르던 이름 모를 노의원을 데려왔을 때는 모든 것이 늦은 후였다.

그는 꼬박 하루를 울었고 가족들을 묻기 위한 구덩이를 팠다. 그리고 자신이 데려온 의원에게 한 가지 부탁을 했다.

“함께 묻어 주십시오. 제가 그리 청했지요.”

문경이 무뚝뚝한 목소리로 말을 받았다.

“그래서 나는 네 뺨을 때려 주었지.”

“많이 아팠습니다. 죽고 싶을 정도로.”

아팠다. 목숨을 좌지우지하는 고통보다는 사랑하는 아내와 아이들을 더 이상 볼 수 없다는 사실 때문에.

“그런 저를 스승님께서 일으켜 세워 주셨습니다.”

문경은 고개를 저었다.

“손을 내밀었을 뿐이다. 그 손을 붙잡고 일어난 것은 네 의지였어.”

“살아야 했습니다. 해야 할 일이 생겼으니까요.”

본래대로라면 목수 역시 역병으로 죽었어야 할 몸이었다.

그러나 의원은 지금껏 본 적 없는 의술로 그를 완치시켰고, 목수는 처음으로 하늘이 정한 생로병사(生老病死)를 한낱 인간 역시 바꿀 수 있음을 깨달았다.

“아직도 눈앞에 선하구나. 제자로 받아 달라며 무릎을 꿇던 네 모습이.”

“이 제자가 기억하는 것과는 다르군요. 저는 따라오라며 손짓하시던 스승님의 모습이 떠오릅니다.”

그렇게 가족을 잃은 젊은 목수는 새로운 목표를 찾았고, 천하를 주유하며 힘없고 가난한 병자를 보살피던 늙은 의원은 새로운 제자를 얻었다.

이제는 의원이 된 목수, 동봉(童奉)이 스승의 진정한 정체를 알게 된 것은 그로부터 오랜 시간이 흐른 뒤였다.

“살성(殺星)…… 실로 무시무시한 별호입니다. 그때 처음으로 스승님이 낯설게 느껴졌지요.”

문경은 무감각한 시선으로 저 너머를 바라봤다.

지금부터 하려는 말은 그가 자신의 제자에게 단 한 번도 묻지 않았던 내용이었다.

“왜 떠나지 않았느냐?”

“제가 스승님을 떠날 것이라 생각하셨습니까?”

“나는 지금까지 헤아릴 수 없이 많은 목숨을 해쳤다. 과거를 숨긴 추악한 살귀(殺鬼)에 불과했지. 네가 떠난다 해도 이해했을 것이다.”

“정말 그랬을지도 모르지요. 하지만 저는 스승님이 어떤 사람인지 너무나도 잘 알고 있었습니다.”

다음 순간, 나지막한 목소리가 이어졌다.

“신의(神醫). 제 스승님은 신의라 불리는 분입니다. 이유 없는 살생을 저지르실 분이 아닙니다.”

“……!”

문경의 눈동자가 파르르 떨렸다. 그건 지금껏 아무에게도 말하지 않았고, 아무도 인정하지 않으려 했던 사실이었다.

그는 살수로 살아오며 정(正), 사(邪), 마(魔)를 가리지 않고 숱한 목숨을 직접 거둬들였다. 그리고 그들은 하나같이 죽어야 할 이유가 있는 자들이었다.

공명정대함으로 이름 높은 정파의 대협은 여인을 간살하는 취미가 있었고, 어느 사파의 고수는 재미 삼아 촌락 하나를 몰살시켰다.

중원을 침공한 마교의 군세가 닥치는 대로 사람들을 죽이고 파괴를 일삼지 않았다면, 보다 못한 천하제일의 살수가 나서서 악명 높은 마두들을 죽이지 않았다면 그는 살성(殺星)이라 불릴 수 없었을 것이다.

“내가 마교와 싸우지 않았다면, 온 천하가 나를 손가락질했을 것이다. 지금껏 그래 왔던 것처럼.”

살성이라는 별호는 천하 무림의 주인이 된 정파가 그에게 내리는 면죄부이자 강자에 대한 찬사일 뿐이었다.

문경은 늘 문경이었음에도, 사람들은 그 이면에 숨겨진 진실을 알지 못했고 알려고도 하지 않았다.

“어째서 알리지 않으셨습니까?”

“모두 지난 일이다. 나는 무림을 떠나고자 했고, 뜻한 바에 따라 의원이 되었지. 그리고 앞으로도 그럴 것이다.”

문경은 천천히 몸을 일으켰다. 어느새 사천당문을 빠져나간 기나긴 행렬은 저 너머로 사라진 후였다.

“이만 내려가자. 우리를 기다리는 병자들이 있다.”

건조한 목소리와 함께 걸음을 뗀 그 순간이었다.

“곧 거대한 전란(戰亂)이 일어날 것입니다.”

문경의 발걸음이 우뚝 멈췄다. 그의 등 뒤로 늙수그레한 제자의 목소리가 이어졌다.

“그때와 같은 일이 반복될 것입니다. 수많은 이들이 죽고 다치겠지요. 부모와 자식을 잃은 자들이 넘쳐나고, 비명과 죽음이 끊이지 않을 겁니다.”

“……많이 바빠지겠군. 준비를 해 둬야겠어.”

“제가 무슨 말을 하려 하는지, 스승님께서는 알고 계시지 않습니까.”

“알고 싶지 않다.”

“스승님.”

“나는 의원이다. 비록 스스로 약속한 바를 깨고 어쩔 수 없이 살생을 저질렀으나, 두 번 다시 그런 실수는 없을 것이다.”

문경은 천천히 말을 이었다.

“싸우는 것은 저들의 몫이고, 병자를 치료하는 것은 우리의 몫이다. 내 뜻은 이미 무림을 떠난 지 오래다.”

“그렇다면 어찌하여 무공을 놓지 않으셨습니까.”

“……!”

문경은 말문이 막혔다.

그건 스스로가 오랫동안 품고 있던 의문이었다. 살생이 싫어 무림을 떠나고자 했다면, 살생을 위한 수단인 무공 역시 전폐해야 맞았다.

그러나 오히려 그의 무공은 한층 진일보했다. 무공에 대한 끈과 미련을 놓지 못했다는 증거다.

‘그것은 어째서인가.’

짧은 상념을 깨트린 것은 늙은 제자의 목소리였다.

“스승님께서는 수백, 수천의 병자를 치료하실 수 있으십니다. 동시에 수만의 인명을 구할 수 있는 분이기도 하지요.”

“…….”

“살성(殺星)이 아닌 신의(神醫)로서 전란을 막아 주십시오. 이 제자는 이곳에서 병자들을 보살피겠습니다.”

문경은 문득 고개를 들어 하늘을 바라봤다.

맑고 푸르르다. 사천당문이 피로 물들었던 칠 주야 전의 하늘은 먹구름으로 가득했었다.

“하늘이 맑구나.”

무뚝뚝한 목소리와 함께 멈춰 있던 발걸음이 앞으로 나아갔다.

“이만 병자들을 살피러 가 보아야겠다. 천천히 내려오너라.”

언덕을 내려가는 그의 등 뒤로 동봉의 목소리가 흩어졌다.

“술시(戌時). 성도의 서쪽 항구에서 출발한다고 했습니다.”

“부질없는 짓. 내가 있어야 할 곳은 무림이 아니다.”

그러나 서서히 멀어지는 스승의 뒷모습을 바라보는 늙은 제자의 입가에는 희미한 웃음이 맺혀 있었다.

“부디…… 강녕하십시오.”

휘이이잉.

어디선가 불어온 바람이 두 사람의 사이를 스쳐 지나갔다.



* * *



“뭘 그렇게 보고 계세요?”

혁무진의 물음에, 항구를 에워싼 인파를 바라보고 있던 나는 고개를 돌렸다.

“별거 아니다. 그냥 혹시나 해서.”

“그러니까 뭘요?”

“이 자식이, 왜 이렇게 꼬치꼬치 캐물어? 그렇다면 그런 줄 알지.”

내 대답에 혁무진이 의미심장하게 웃었다.

“사실 다 알고 있습니다. 조장님께서 왜 그러시는지.”

“……?”

순간 멈칫했다. 이 자식이 어떻게 그걸 알지? 나와 신의가 나눈 대화는 청풍도 듣지 못했는데.

‘이 녀석 눈치가 이렇게 빨랐나.’

의아해하던 그때, 녀석이 작게 속삭였다.

“저기 앞줄 우측 네 번째에 서 있는 소저를 보고 계셨던 거 아닙니까?”

“…….”

“확실히 예쁘긴 하네요. 제법 있는 집 규수 같아 보이는데. 조장님께서 허락하신다면 오른팔인 제가 슬쩍 가서 따로 자리를…….”

“무진아.”

“예? 아, 혹시 자연스러운 만남을 추구하시는 쪽입니까? 그렇다면…….”

“장강 밑바닥에 가라앉고 싶니?”

“……!”

“개소리하지 말고 계속 거기 누워 있어. 나중에 멀미 난다고 토하지나 말고.”

“……옙.”

조용히 찌그러지는 혁무진의 모습에 궁기방이 킬킬거렸다.

“멍청한 작자 같으니. 우측 네 번째가 아니라 좌측 세 번째 여인이다. 누가 봐도 훨씬 미인인데 눈깔이 삐었군.”

“눈깔 삐꾸 만들어 줘?”

“……미안하다.”

“사람답게 살자. 사람답게.”

한숨과 함께 고개를 내저은 나는 마지막으로 구름처럼 모여 있는 사람들을 쭉 훑었다.

확실히 둘 다 예쁘긴 하지만 궁기방이 말한 좌측 세 번째가 내 스타일…… 아, 이게 아니지.

‘아 씨, 저 자식들이 떠들어 댄 것 때문에 괜히 자꾸 보게 되네.’

그런 생각을 하고 있을 때, 구릿빛 체구의 거한이 내게 다가와 말을 건넸다.

“이보게, 후배. 아니 후배가 아니라 진 소협, 아니 대협.”

뭐야, 버퍼링이야?

나는 번개에 콩 볶듯 호칭을 바꿔 대는 선화아(船火兒) 무송에게 해결책을 제시해 주었다.

“그냥 후배라고 하시죠.”

“커흠. 그, 그래도 되겠나?”

“안 될 건 뭡니까. 전에는 잘만 하시더니.”

“그래도 그, 자네가 워낙 큰일을 해내지 않았나.”

그렇긴 하다. 산서잠룡이라는 지역구 후기지수에서 이제는 전국구 유명인사가 되었으니까.

“그리고 적 대협께서도 나를 좀 별로 마음에 안 들어 하시는 것 같길래…….”

“괜찮아요. 애초에 물을 별로 안 좋아하셔서.”

무송이 힐끔거리는 곳에는 잔뜩 성난 얼굴의 적천강이 있었다.

바로 옆에는 진위경이 뭔지 모를 죽간을 들여다보고 있고, 청풍은 미미에게 새로운 기술을 연습시키고 있었다.

“미미, 파도타기!”

취릭, 촤아아악!

……저거 물뱀이었나.

좀처럼 보기 힘든 진귀한 광경에 잠시 시선을 뺏겼던 무송이 떨떠름하게 입을 열었다.

“어쨌든, 출항 준비는 이미 끝마쳤는데 언제쯤 출발하면 되겠나?”

“혹시 지금 시간이?”

“자네가 말했던 술시가 지났네. 더 어두워지기 전에 출발하는 것이 좋아.”

“……음.”

“혹시 더 올 사람이라도 있는 건가?”

무송의 질문에 잠시 고민하던 나는 고개를 저었다.

“아뇨. 없어요.”

“그럼 출발해도 되겠군.”

“그렇게 하시죠.”

“알겠네.”

무송이 손을 번쩍 치켜올리자 이미 모든 준비를 끝마친 수적들이 일사불란하게 움직였다.

환송을 위해 모여 있던 사람들이 우리를 향해 손을 흔들던 바로 그 순간이었다.

“잠깐, 잠깐만요!”

“정지, 정지!”

항구에서 떨어지려던 쾌조선의 뱃머리가 흔들렸다.

나는 저 멀리, 사람들 사이를 해치며 다가오는 한 소년을 발견하고 피식 웃었다.

“한 사람만 더 태우고 가죠.”
```

## Final English reading copy

```markdown
# Chapter 376

A sea of people.

There was no other way to describe the scene.

Word had spread that the Sleeping Dragon of Shanxi—or rather, the Blazing Fire Divine Dragon, Jin Taekyung—and the Huashan Divine Dragon, Cheongpung, were leaving, and people had gathered in clouds.

Not only martial artists, but fearless commoners as well, had come out to see them off. The crowd stretched farther and farther, an endless tail that could not be counted.

“Safe travels, Blazing Fire Divine Dragon!”

“The martial world of Sichuan will never forget you!”

“It’s a snake with horns! The Huashan Divine Dragon has a snake with horns!”

“Whoa! The snake just did a somersault in midair!”

“The Fire King! The Fire King is holding the snake and trying to set it on fire!”

The murmuring noise gradually faded as the procession moved farther away.

And on a deserted hilltop, a boy sitting on a tree stump and watching the entire scene suddenly spoke.

“We’ve come a long way.”

“We certainly have. It’s tiring.”

At the sight of the old disciple plopping down on the grass with ragged breaths, the boy, Mungyeong, muttered,

“…We really have come a long way.”

He was not talking about distance. Mungyeong was talking about the years they had traveled through.

“Do you remember when we first met?”

“How could I forget?”

The old disciple wiped the sweat from his brow. It was as though the scorching sunlight from that day were beating down on him again.

“The first year of Hongwu. That exceptionally hot summer.”

It was the year the civil war over the imperial throne ended and a new emperor ascended.

The young and ambitious emperor changed the era name and attempted reforms, but the people, exhausted by the long civil war, were far too weary to heed the emperor’s will and take part in those reforms.

“Rebellions broke out across the land, and bandits ran rampant.”

“There was a drought, and swarms of locusts swept across the plains. The corpses of government soldiers and rebels filled the roads, and epidemics spread everywhere.”

“Yes. It was truly an age of turmoil.”

Death gave birth to more death, and soon it devoured the entire continent.

A young carpenter with the surname Dong could not escape the dark shadow that hung over the land, either.

“I still think about that time from time to time.”

The decades had changed more than just the landscape. The young carpenter who had lost his beloved wife and two children to the epidemic had since become an old physician.

“I wonder if I could have saved my family if I had been just a little faster. If I had found you sooner.”

“Do you regret it?”

“Yes.”

Sitting on a hill close to the heavens and gazing at the drifting scraps of cloud, the old physician’s eyes had returned to those of the young carpenter.

“For as long as I have breath in my body.”

It had been only a single day.

By the time the carpenter, dragging along his plague-stricken body, brought back the nameless old physician who had been staying in the slash-and-burn settlers’ village, everything was already too late.

He cried for an entire day, then dug a pit to bury his family. And he made one request of the physician he had brought.

“Bury me with them. That was what I asked.”

Mungyeong answered in his blunt voice.

“And so I slapped you across the face.”

“It hurt. Enough to make me want to die.”

It had hurt. Not because of pain that threatened his life, but because he could no longer see his beloved wife and children.

“You were the one who made me stand again, Master.”

Mungyeong shook his head.

“I merely held out my hand. You were the one who took it and stood.”

“I had to live. I had something to do.”

The carpenter’s body should have died from the epidemic.

But the physician cured him with medical knowledge unlike anything he had ever seen, and for the first time, the carpenter realized that even a human being could alter the birth, aging, sickness, and death ordained by heaven.

“I can still see it clearly. You kneeling before me and asking me to accept you as my disciple.”

“I remember it differently. I remember you beckoning me to follow you, Master.”

Thus, the young carpenter who had lost his family found a new goal, while the old physician who traveled the world caring for the sick and poor gained a new disciple.

It was only much later that the carpenter, who had now become a physician himself, learned his master’s true identity.

“Slaughter Saint… It is a truly terrifying sobriquet. That was the first time you felt like a stranger to me, Master.”

Mungyeong gazed into the distance with an emotionless expression.

What he was about to ask was something he had never once asked his disciple.

“Why didn’t you leave?”

“Did you think I would leave you?”

“I have taken countless lives over the years. I was nothing more than an ugly slaughter demon hiding my past. I would have understood if you had left.”

“Perhaps I really would have. But I knew all too well what kind of person you were, Master.”

A moment later, his low voice continued.

“The Divine Physician. My master is known as the Divine Physician. You are not someone who would kill without reason.”

“…”

Mungyeong’s eyes trembled.

It was a truth he had never told anyone, and one that no one had ever been willing to acknowledge.

He had lived as an assassin, taking countless lives with his own hands, whether they belonged to the orthodox faction, the unorthodox faction, or the Demonic Cult. And every one of those people had had a reason they deserved to die.

A Great Hero of the orthodox faction, renowned for his fairness and integrity, had made a hobby of raping and murdering women. A master of an unorthodox faction had slaughtered an entire village for fun.

If the army of the Demonic Cult invading the Central Plains had not killed and destroyed indiscriminately, and if the greatest assassin under heaven had not stepped forward to kill those infamous demon heads because he could no longer stand by and watch, he could never have been called the Slaughter Saint.

“If I had not fought the Demonic Cult, the entire world would have pointed fingers at me. Just as it had always done.”

The title of Slaughter Saint was merely an absolution granted by the orthodox faction that ruled the Murim—and praise for a powerful man.

Mungyeong had always been Mungyeong, but people neither knew nor wanted to know the truth hidden beneath the surface.

“Why didn’t you tell them?”

“It is all in the past. I wanted to leave the Murim, and I became a physician as I had intended. I will continue to do so.”

Mungyeong slowly rose to his feet. By then, the long procession that had left the Sichuan Tang Clan had disappeared into the distance.

“Let’s go down. There are patients waiting for us.”

He had just started walking, his voice dry, when—

“A great war will break out soon.”

Mungyeong came to an abrupt stop. Behind him, the old disciple’s voice continued.

“The same thing that happened back then will happen again. Countless people will die or be injured. There will be countless people who have lost their parents or children, and the screams and deaths will never end.”

“…I suppose I’ll be very busy. I should make preparations.”

“You know what I am trying to say, Master.”

“I do not want to know.”

“Master.”

“I am a physician. Though I broke the promise I made to myself and killed when I had no other choice, I will never make that mistake again.”

Mungyeong continued slowly.

“Fighting is their responsibility, and treating the sick is ours. My heart left the Murim long ago.”

“Then why did you never abandon your martial arts?”

“…”

Mungyeong was at a loss for words.

It was a question he himself had carried for a long time. If he had wanted to leave the Murim because he hated killing, then it should have been right for him to abandon martial arts as well—the means by which he killed.

Yet his martial arts had advanced even further. It was proof that he had been unable to let go of his attachment to them.

*Why was that?*

The old disciple’s voice broke through his brief reverie.

“You can treat hundreds, even thousands, of patients, Master. At the same time, you are capable of saving tens of thousands of lives.”

“…”

“Please prevent the coming war—not as the Slaughter Saint, but as the Divine Physician. This disciple will care for the patients here.”

Mungyeong suddenly lifted his head and looked at the sky.

It was clear and blue. Seven days and nights earlier, when the Sichuan Tang Clan had been dyed in blood, the sky had been filled with dark clouds.

“The sky is clear.”

With his blunt voice, he resumed his halted steps.

“I should go check on the patients. Come down slowly.”

Behind him as he descended the hill, Dongbong’s voice scattered into the wind.

“The Hour of the Dog. They said they would depart from the western port of Chengdu then.[^1]”

“Pointless. The Murim is not where I belong.”

Yet as the old disciple watched his master’s back gradually disappear into the distance, a faint smile formed around his lips.

“Please… stay well.”

Whoooosh.

A wind that had come from somewhere swept between the two men.

* * *

“What are you looking at so intently?”

At Hyuk Mujin’s question, I turned away from the crowd surrounding the port.

“Nothing. Just in case.”

“Then what are you looking at?”

“You little pest. Why are you interrogating me like this? If I say it’s nothing, take it as nothing.”

Hyuk Mujin gave me a meaningful smile.

“I actually know why you’re acting that way, Squad Leader.”

“…?”

I froze for a moment. How the hell did he know? Even Cheongpung hadn’t heard the conversation between the Divine Physician and me.

*Since when was this guy so perceptive?*

As I wondered about it, he whispered,

“Weren’t you looking at the young lady standing fourth from the right in the front row?”

“…”

“She is pretty, that’s for sure. She looks like the daughter of a fairly wealthy family. If you give me permission, Squad Leader, I could quietly go over there as your right-hand man and arrange a separate—”

“Mujin.”

“Yes? Ah, do you prefer natural encounters? If so…”

“Do you want to sink to the bottom of the Yangtze?”

“…”

“Stop talking nonsense and keep lying there. And don’t puke later because you get seasick.”

“…Yes, sir.”

As Hyuk Mujin quietly shrank in on himself, Gung Gibang snickered.

“What a fool. It’s not the fourth woman on the right, but the third on the left. Anyone can see she’s much prettier. Your eyes must be crooked.”

“Want me to make them crooked for real?”

“…Sorry.”

“Let’s live like human beings. Like human beings.”

With a sigh, I shook my head and gave the crowd gathered like clouds one last sweeping look.

The women on both sides were definitely pretty, but the third from the left was more my type—

*No. That’s not what this is about.*

*Damn it. Those idiots keep talking about it, so now I can’t stop looking.*

That was when a towering, bronze-skinned man approached me and spoke.

“Hey there, junior. No, not junior. Young Hero Jin. No, Great Hero.”

*What is this, buffering?*

I offered a solution to the boatman Mu Song, who was switching forms of address at lightning speed.

“Just call me junior.”

“Ahem. Th-That would be all right?”

“Why wouldn’t it be? You used to do it just fine.”

“Even so, you’ve accomplished such a great thing.”

He had a point. I had gone from being a local rising martial artist known as the Sleeping Dragon of Shanxi to a nationwide celebrity.

“And Great Hero Jeok seems not to like me very much, either…”

“It’s fine. He never liked water much in the first place.”

Where Mu Song kept glancing, Jeok Cheongang stood with a face twisted in fury.

Right beside him, Jin Wikyung was examining some bamboo slips whose contents I could not identify, while Cheongpung was teaching Mimi a new trick.

“Mimi, ride the waves!”

Sssrik—splash!

…Was that a water snake?

Mu Song, whose attention had been stolen for a moment by the rare spectacle, finally spoke with a sour expression.

“In any case, we have finished preparing for departure. When should we leave?”

“Has the time come already?”

“The Hour of the Dog you mentioned has passed. It would be best to leave before it gets any darker.”

“…Hmm.”

“Is someone else coming?”

I considered Mu Song’s question for a moment, then shook my head.

“No. No one.”

“Then we can depart.”

“Let’s do that.”

“Very well.”

Mu Song raised one hand high, and the water bandits, who had already finished preparing everything, began moving in perfect unison.

The people gathered to see us off were waving in our direction when—

“Wait! Just a moment!”

“Stop! Stop!”

The bow of the fast ship, which was about to pull away from the port, rocked.

Far in the distance, I spotted a boy making his way through the crowd and let out a quiet laugh.

“Let’s take one more passenger.”

[^1]: The Hour of the Dog was a traditional two-hour period, roughly corresponding to 7–9 p.m.
```
