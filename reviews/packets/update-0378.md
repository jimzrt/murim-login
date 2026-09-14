<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0378.txt",
      "sha256": "962bd52f1b903b50cf75748c160b649bef3de97e2e63ac797847b344fc841bc6",
      "bytes": 13072
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3ee571ca9ae8e0de4d9538954058cc39664042ad01a014522aeb87f460ab0f08",
      "bytes": 6113
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7874e96fdf8ef432dcd7496baa1361f81ee489eaf6ad592a91db5ad180635298",
      "bytes": 6718
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "77b9a99377a6da8695977c151cf6c0db1d29f65c63142bd7d561c10d9ee32168",
      "bytes": 23777
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8c56e39fdc54b30b20be882ea01b04bfa96073319cc4ae5b03e7ce4e9538bab7",
      "bytes": 4415
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 12130
}
-->

# Durable State Update — Chapter 378

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 378. Keep at most
2 continuity_sources. Use only chapter
numbers through 378. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 378,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 378,
    "continuity_sources": [378],
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
    "The Myriad Poison Ring was transferred to Taekyung by Tang Sadok and is now bound to him; White Flame, Myriad Poison Ring, and Flame Dragon Armor are currently bound.",
    "Mungyeong is the Divine Physician and the Slaughter Saint. He has left the Murim's affairs behind, intends to live as a physician, and is the master of Dongbong.",
    "Dongbong is Mungyeong's longtime disciple and a physician who lost his wife and two children to an epidemic before Mungyeong cured him and accepted him as a disciple.",
    "A hidden, currently inactive transport formation associated with Dark Heaven was found near Sichuan; its origin and function remain unresolved.",
    "Jin Wikyung has proposed relocating the Sichuan Tang Clan and has been assigned to escort Samgoe toward Henan.",
    "Taekyung's return to his original world is imminent, with roughly six hours having passed there; aboard the ships, he initiated Logout, but the chapter does not explicitly establish the result after the countdown.",
    "Cheongpung is Mimi's temporary guardian while the Tang Clan's future is uncertain.",
    "The Divine Physician, referred to in Taekyung's joke as Dongbong, has asked Taekyung for time before his departure; the request remains undisclosed.",
    "Dongbong predicts that a great war will soon occur and asks Mungyeong to prevent it as the Divine Physician; Mungyeong verbally refuses and says the Murim is not where he belongs, while the announced departure from Chengdu's western port remains unresolved.",
    "Taekyung and Cheongpung are preparing to leave Sichuan by fast ship from Chengdu's western port after the Hour of the Dog.",
    "Mu Song is the boatman associated with the water bandits preparing the ship.",
    "An unidentified boy reaches the port immediately before departure and is accepted as one more passenger.",
    "The Sichuan Governor's favorite concubine Ae-hyang manipulated him into concealing the government uniforms and weapons involved in the recent martial-artist conflict and preparing a false memorial that exaggerates his role in restoring order. A sinister red light entered her eyes, and she appears to serve an unidentified superior."
  ],
  "continuity_sources": [
    377
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved in the accepted local anchor.",
    "Dark Heaven's agents, purpose, and connection to the transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination remain unresolved.",
    "The outcome and timing of the planned Samgoe escort to Henan remain unresolved.",
    "The matter the Divine Physician wants to discuss with Taekyung before his departure remains unresolved.",
    "The identity of the boy who arrives at the port and whether he will accompany Taekyung's group remain unresolved.",
    "Whether Mungyeong will ultimately intervene in the coming war or leave the Murim remains unresolved.",
    "The identity of Ae-hyang's superior and the nature of her sinister red-eyed influence remain unresolved.",
    "Whether the Sichuan Governor submits the false memorial and what consequences follow remain unresolved.",
    "What follows Taekyung's Logout countdown remains unresolved."
  ],
  "safe_through": 377,
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
    "Retain Master for 스승님 and render 살귀 as slaughter demon in Mungyeong's self-description.",
    "Render 식경 as sikgyeong, approximately thirty minutes, with a footnote.",
    "Render 흑룡갑 as Black Dragon Armor, 화룡갑 as Flame Dragon Armor, 수룡채 as Water Dragon Stronghold, 열화신공 as Blazing Flame Divine Art, 상산왕 as King of Shangshan, and 삼공 as Grand Councilor."
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
| 애향 | **Ae-hyang** | The Sichuan Governor's favorite concubine; covertly manipulative. |
| 상산왕 | **King of Shangshan** | Noble whose token was carried by Taekyung's group. |
| 수룡채 | **Water Dragon Stronghold** | Stronghold whose flag flies from the ships carrying Taekyung's group. |
| 흑룡갑 | **Black Dragon Armor** | The armor's former name; only a fragment survives. |
| 화룡갑 | **Flame Dragon Armor** | New name Taekyung gives the bound armor fragment. |
| 열화신공 | **Blazing Flame Divine Art** | Art whose formula Taekyung uses to infuse the armor. |
| 삼공 | **Grand Councilor** | High office referenced in the Sichuan Governor's ambitions. |

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
| 사천성주 | 애향 | lover_to_favorite_concubine | Ae-hyang | intimate-affectionate | The Sichuan Governor repeatedly calls his favorite concubine by name and speaks to her in an indulgent intimate manner. |
| 애향 | 사천성주 | favorite_concubine_to_lover | my dear | intimate-coquettish | Ae-hyang addresses the Sichuan Governor as 가가 while flattering and manipulating him. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 시스템              | **System**                     |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 377
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃378화



띠링.



- [로그아웃]을 성공적으로 완료했습니다.



경쾌한 시스템 알림과 함께, 잠시 떨어져 나갔던 감각들이 돌아오기 시작했다.

등을 타고 전해지는 침대의 푹신함, 전용기 내부의 따뜻한 공기.

그리고 내 양어깨를 잡고 흔드는 누군가의 손길과 외침까지.

“진태경 씨! 일어나십시오! 진태경 씨!”

- 일어나라! 간악한 인간아!

귓가를 파고드는 다급한 두 사람, 아니 한 몬스터와 인간의 목소리에 눈동자를 깜빡였다.

선명해지는 시야 속, 익숙한 얼굴이 눈에 들어왔다.

“어, 최 팀…….”

쫘악!

“일어나라고!”

- 잘했다! 조금 덜 간악한 인간이여!

“…….”

뭐야, 이거.

생각지도 못한 따귀 한 방을 얻어맞은 나는 얼떨떨한 목소리로 대답했다.

“저 일어났는데…….”

“도대체 어떻게 된 사람입니까! 그렇게 깨웠는데 왜 이제야 일어나요!

- 죽어, 그냥 죽어!

“죄, 죄송…….”

박력 보소. 이 정도로 극대노한 최 팀장을 보는 건 처음이다.

무슨 일이 벌어져도 침착을 유지하며 명품이나 자랑하던 최 팀장의 눈에서 번갯불이 튀고 있었다.

‘그런데 왜 저래. 아직 비행기 안인 것 같은데.’

엉겁결에 사과하긴 했는데, 이게 따귀까지 맞을 일인가 싶어 어리둥절하던 그 순간.

“지금 이럴 때가 아닙니다! 어서……!”

“꺄아아악!”

이어지려던 최 팀장의 목소리가 스튜어디스들의 비명에 파묻혔다. 조종사로 짐작되는 남자들의 외침이 뒤를 이었다.

“메이데이! 메이데이! 메이데이!”

“관제탑! 관제타아압!”

“……뭐여, 시벌.”

도대체 지금 무슨 일이 벌어지고 있는 거지?

정신없이 주위를 둘러보는 내게, 최 팀장의 믿을 수 없는 한마디가 날아들었다.

“몬스터의 습격입니다!”

“몬스터? 습격?”

뭔 개소리야. 우리는 중국 중앙위원회에서 보내 준 전용기를 타고 2만 5천 피트 상공을 날아가는 중이었는데.

지금쯤이면 목적지인 쓰촨성 청두 국제공항이 보여도 이상하지 않을…….

“어?”

무심코 고개를 돌려 창밖을 확인한 나는 멍하니 입을 벌렸다.

까마득한 높이로 내려다보이는 거대한 규모의 공항에서, 불길이 솟구치고 크고 작은 점들이 움직였다.

전투다. 인간과 몬스터 간의 죽고 죽이는 전투가 벌어지고 있었다.

심지어 그것으로 끝이 아니었다.

- 캬우우우우!

내가 타고 있는 전용기를 향해 빠르게 가까워지는 몬스터의 거대한 동체.

“저건…….”

틀림없다. 두 눈을 비비고 다시 봐도 와이번(Wyvern)이다.

드레이크와 함께 용족(龍族)으로 분류되는 A급 몬스터.

물론 땅에서 만나도 지랄 같지만, 2만 5천 피트 상공에서는 더더욱 만나기 싫은 놈들이 나타났다.

그것도 무려 십여 마리나!

‘……이게 무슨 개 같은 상황이야.’

지상에서는 청두 국제공항을 둘러싼 치열한 전투가 벌어지고, 2만 5천 피트 상공에서는 와이번 무리가 내가 탄 전용기를 쫓아 오고 있다.

잠깐 정지했던 두뇌가 결론을 도출해 내기까지는 그리 오랜 시간이 필요하지 않았다.

“리치(Rich)!”

나도 모르게 벼락처럼 튀어나온 외침.

현대 시간으로 일주일 전, 유례없는 몬스터 웨이브와 함께 나타난 최상위 언데드 몬스터가 어느새 여기까지 마수를 뻗친 것이 틀림없었다.

“관제탑이 응답하지 않습니다!”

“와이번이, 와이번이……!”

“끼아아아악!”

- 내 이럴 줄 알았다! 우린 이제 다 죽은 목숨이야!

나는 당황한 와중에도 스켈레톤 워로드의 말을 정정해 주었다.

“맞는 말이긴 한데, 넌 이미 죽은 목숨 아니었냐?”

- 닥쳐라, 이 간악한 인간! 모든 게 너 때문이다! 아아, 군단이여! 본 사령관을 용서하라!

몬스터고 인간이고 할 것 없이 패닉에 빠진 비명과 고함이 사방에서 빗발쳤다.

이들 중 그나마 이성을 유지하고 있는 건 한 사람뿐이었다.

“모두 진정하세요! 걱정하시는 일은 일어나지 않을 겁니다!”

역시 최 팀장, 믿음직하다. 분명 이 위기를 타개할 만한 수를 생각해냈음이 틀림없다.

침착한 어조로 혼란을 가라앉힌 최 팀장이 나를 가리켰다.

“여기 계신 진태경 씨가 해결해 줄 겁니다!”

“……?”

“진태경 씨. 어떻게 해야 합니까?”

“아니, 왜 그걸 저한테…….”

“저는 진태경 씨를 믿습니다!”

“…….”

그러니까 왜 날 믿냐고. 지금 같은 상황이면 하느님이나 부처, 알라를 믿는 게 더 도움이 될 것 같은데.

순간 할 말을 잃은 나를 향해 사람들의 시선이 우수수 날아와 꽂힌다.

“그, 그러고 보니 저 헌터님에 관해서 들은 적이 있어. 샤오 양 주석 동지께서도 특별히 요청할 만큼 대단한 실력자라던데.”

“저도 소문은 들었습니다. 어쩌면 새로운 S급 헌터일지도 모른다고. 네임드 몬스터를 둘씩이나 혼자서 잡았대요.”

“오오, 오오오!”

“살았다! 우린 살았어!”

- 너, 간악한 인간! 강한 줄은 알았지만 상상 이상이로군! 기뻐하라, 군단이여. 본 사령관은 살았다!

“……넌 이미 죽었다니까.”

미치겠네. 이미 전부 다 제정신이 아니다. 나는 어처구니없는 눈빛으로 최 팀장을 바라보았다.

“도대체 뭘 믿고 이러는 겁니까?”

최 팀장이 망설임 없이 대답했다.

“말했잖습니까. 진태경 씨를 믿는다고요.”

“그러니까 그 근거 없는 믿음이 어디서…….”

“근거 있는 믿음입니다.”

“예?”

“지금 같은 상황에서 진태경 씨가 보여 주는 태도, 말투, 표정. 그 모든 것들이 제 믿음에 대한 근거입니다.”

“……!”

그제야 비로소 깨달을 수 있었다. 지금의 나는 예기치 못한 상황에 당황했을 뿐, 그 어떤 두려움이나 공포도 느끼지 못하고 있다는 사실을.

정답은 생각보다 가까이에 있다.

‘강하니까.’

나는 강하다. 더욱더 강해졌다. 그 어떤 위험도 피해 갈 수 있을 만큼.

그것이 지상을 파도처럼 휩쓸고 있는 몬스터들도, 바짝 뒤를 쫓아오는 와이번 무리도 두렵지 않은 이유였다.

“그렇다는 거지…….”

내심 작게 중얼거린 나는 입을 열었다.

“기장이 누굽니까?”

내 물음에 저 앞 조종석에서 손 하나가 불쑥 솟아올랐다.

바들바들 떨리는 손. 나머지 한 손으로는 필사적으로 조종간을 붙잡고 달려드는 와이번을 피하려 안간힘을 쓰고 있을 것이다.

“저, 접니다만.”

“잠깐만 문 열어도 돼요?”

“예?”

“비행기 문 좀 열어도 되냐고요.”

얼마나 충격적이었는지, 기장이 미친놈 보는 듯한 시선으로 고개를 내밀었다.

“당연히 안 됩니다! 기압 차단 장치 때문에 열지도 못할뿐더러, 기체가 기압을 감당하지 못하고 파손될 겁니다! 그러면 호흡도 제대로 할 수 없어요!”

최 팀장이 손가락에 끼고 있던 반지를 만지작거리며 끼어들었다.

“기압은 제가 막을 수 있을 것 같습니다. 무슨 생각이신지는 모르지만 한 번 해보시죠.”

“오케이.”

“하지 말라고! 이 빵즈(棒子) 놈들아! 우릴 다 죽일 셈이냐!”

“……뭐, 빵즈?”

감히 자랑스러운 대한의 김치맨 앞에서 한국인을 비하하는 말을 하다니.

무심코 튀어나온 말실수를 알아차린 기장의 얼굴이 하얗게 질렸다.

“아니, 그게 아니고.”

“짱깨 새끼가. 팍 씨.”

“……!”

“야, 기장!”

“예, 예?”

“연다?”

“앗. 아앗!”

기장이 말릴 틈도 없이 나는 문을 열었다. 아니, 잘랐다.

스걱!

강기(劍罡). 현대에서는 오라 블레이드(Aura Blade)라 불리는 그것이 단단한 합금을 가르며 작은 문을 만든다.

무림의 초절정 고수가 그렇듯, 이곳에서는 S급 헌터만이 보여 줄 수 있는 강대한 힘.

최 팀장의 눈동자가 경악으로 부릅떠졌다.

“진태경 씨, 이건……!”

“팀장님!”

콰아아아아!

지금 놀라고 있을 때가 아니다. 엄청난 바람과 기압으로 기체가 휘청이고 기내는 엉망이 되고 있었으니까.

사람들의 비명과 내 외침에 정신을 차린 최 팀장이 반지를 문질렀다.

“빈틈없는 장벽이 주위를 감싼다. 배리어(Barrier)!”

“오.”

주문 영창과 함께 투명한 기의 막이 새로운 입구를 물 샐 틈 없이 가로막았다.

이런 방법이 있었구나. 나는 짧은 감탄과 함께 기내 밖으로 상반신을 내밀었다.

나를 아군으로 인식한 최 팀장의 배리어 마법은 아무런 제지 없이 통과시켜 주었다.

쿠구구구구!

압사라도 시킬 것처럼 상반신을 후려치는 풍압에 나는 씩 웃었다.

‘이거, 장난 아닌데?’

하지만 못 견딜 정도는 아니다.

아니, 내가 못 견디는 것이 오히려 이상했다. 서천마군이 내뿜던 기파에 비교하면, 이 정도는 살랑거리는 봄바람이나 다름없었으니까.

- 캬우우우우!

바로 그 봄바람에, 몬스터의 날카로운 괴성이 섞여 들어온다.

나는 어느새 지척까지 다가온 와이번 무리를 보며 거리를 가늠했다.

‘약 백여 미터. 한 번도 해 본 적은 없지만…… 이 정도 거리라면 충분하겠지.’

인벤토리 오픈. 장착.

스윽.

헌터 마켓에서 할인 구매한 창 한 자루가 손아귀에 잡힌다.

나는 창 던지기 선수처럼 어깨를 한껏 뒤로 젖혔다. 허리부터 손목까지. 필요한 근육과 힘줄이 활시위처럼 팽팽하게 당겨졌다.

- 캬우우!

뭔가 이상함을 눈치챈 선두의 우두머리 와이번이 괴성과 함께 고개를 젖혔다.

새하얀 기류가 놈의 주둥이를 향해 빨려 들어가는 것이 보였다.

‘저건…….’

- 브레스! 브레스다! 피해라, 간악한 인간이여!

스켈레톤 워로드의 외침은 정답이었다.

무수히 많은 몬스터 중에서도 오직 용족에게만 허락된 권능. 바로 브레스(Breath)가 쩍 벌어진 주둥이 안에서 형체를 갖추는 광경이 똑똑히 보였다.

고오오옹.

거대한 바람의 구(球). 금속을 종잇장처럼 갈기갈기 찢어 버릴 수 있는 에어 브레스가 완전한 형체를 갖춘 그때.

“야, 와이번!”

- 캬우?

“넣는다!”

나는 벼락처럼 외치며 한껏 젖혔던 어깨를 전방으로 뿌렸다.

화륵, 쐐애애애액!

창날에 서린 화염의 강기가 공기를 태우고 바람을 가른다.

일직선으로 뻗어 나가는 청백색의 빛줄기에, 와이번의 샛노란 눈동자가 크게 뜨였다.

- 키이이익!

후우우웅!

창날의 끝에서 터져 나가는 압축된 공기. 새하얀 구름. 그리고…….

퍼걱! 퍼버벙!

마치 실이 끊어진 연처럼, 지상을 향해 추락하는 거대한 동체가 있었다.



* * *



- 캬우?

- 키잇?

십여 쌍의 샛노란 눈동자들이 서로를 바라본다.

날 때부터 흉포하기 짝이 없는 와이번이지만, 지금 이 순간만큼은 당혹감에 사로잡혀 어찌할 바를 몰랐다.

- 키키킷?

- 키익…….

뭐야, 대장 죽은 거야?

아마 그런 것 같은데…….

자신들만의 대화를 주고받은 와이번들은 황당했다.

그들의 우두머리는 동족 중에서도 ‘검은 별’이라 불릴 만큼 강한 존재였다.

그리고 지금, 검은 별은 검은 점이 되어 까마득한 지상으로 추락하는 중이었다.

- 키리릭?

- 크르르륵.

심지어 어떻게 죽었는지 제대로 본 놈도 없었다.

다만 저 콩알만 한 인간 하나가 창을 던져서 맞추지 않았나 짐작할 뿐이다.

하지만 말도 안 되는 소리다.

어떻게 인간 따위가 감히 위대한 드래곤의 후예를…….

“야, 거기 그린 와이번!”

- 키릭?

“넣을게!”

퍼걱!

이번에는 똑똑히 볼 수 있었다. 빛줄기에 터져 나가는 동료의 머리통을.

- 키릭!

- 캬우우우!

대장에 이어 또 다른 혈족이 죽다니!

극도로 분노한 와이번들은 저 빌어먹을 인간에 대한 복수를 다짐했다.

- 키잇!

물론 오늘은 아니고. 나중에, 조금 더 나중에 복수하기로.

“야, 거기 블루 와이번!”

퍼걱!

……복수, 할 수 있을까?

십여 쌍의 날개가 필사적으로 퍼덕이기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 378

Ding.

> **System**
>
> You have successfully completed **Logout**.

Along with the cheerful system notification, the sensations that had briefly slipped away began returning.

The softness of the bed against my back. The warm air inside the private jet.

And the hands gripping and shaking both my shoulders, along with the shouts that came with them.

“Mr. Jin Taekyung! Wake up! Mr. Jin Taekyung!”

- Wake up, you vile human!

I blinked at the urgent voices drilling into my ears—two voices, no, one monster’s and one human’s.

As my vision cleared, a familiar face came into view.

“Uh, Team Lea—”

Smack!

“Wake up!”

- Well done! You’re a slightly less vile human now!

“…”

What the hell was this?

After taking an unexpected slap across the face, I answered in a dazed voice.

“I’m awake…”

“What is wrong with you? I tried so hard to wake you up, so why are you only getting up now?”

- Just die! Go ahead and die!

“S-Sorry…”

Talk about force. This was the first time I’d ever seen Team Leader Choi this furious.

No matter what happened, Team Leader Choi had always kept his composure while showing off his designer goods. But lightning was practically shooting from his eyes.

*What’s gotten into him? We’re still on the plane, aren’t we?*

I had apologized on instinct, but I was still bewildered. Was this really something worth getting slapped over?

That was when—

“This is no time for this! Hurry and—”

“Aaaah!”

Team Leader Choi’s voice was swallowed by the flight attendants’ screams. The shouts of men who were probably the pilots followed.

“Mayday! Mayday! Mayday!”

“Control tower! Control towerrrr!”

“…What the fuck?”

What on earth was happening?

As I frantically looked around, Team Leader Choi delivered an unbelievable statement.

“We’re under attack by monsters!”

“Monsters? An attack?”

What kind of bullshit was that? We were flying at twenty-five thousand feet in a private jet sent by the Central Committee of China.

By now, it wouldn’t have been strange for our destination, Chengdu International Airport in Sichuan Province, to come into view…

“Huh?”

I unconsciously turned toward the window—and stared with my mouth hanging open.

Far below, a massive airport stretched across the ground. Flames surged into the sky, while large and small dots moved through the chaos.

It was a battle. A deadly battle between humans and monsters.

And that wasn’t all.

- Kyaaaauuu!

The enormous body of a monster was rapidly closing in on the private jet I was riding in.

“That’s…”

There was no mistaking it. Even after rubbing my eyes and looking again, it was still a wyvern.

An A-rank monster classified as part of the dragonkin alongside drakes.

They were a pain in the ass even on the ground, but at twenty-five thousand feet, they were the last things I wanted to encounter.

And there were around a dozen of them!

*…What kind of fucked-up situation is this?*

A fierce battle was raging around Chengdu International Airport below, while a flock of wyverns chased the private jet carrying me through the sky.

It didn’t take long for my briefly frozen brain to reach a conclusion.

“Lich!”

The shout burst from me like a thunderbolt.

There was no doubt about it. The supreme undead monster that had appeared alongside an unprecedented monster wave one week ago in modern-world time had extended its reach this far.

“The control tower isn’t responding!”

“The wyverns! The wyverns are—!”

“Kyaaaah!”

- I knew this would happen! We’re all dead!

Even in the middle of my panic, I corrected the Skeleton Warlord.

“That’s true, but weren’t you already dead?”

- Shut up, you vile human! This is all your fault! Ahhh, my legion! Forgive your commander!

Screams and shouts rained down from every direction as humans and monsters alike fell into a panic.

Only one person among them managed to retain his sanity.

“Everyone, calm down! The thing you’re afraid of won’t happen!”

As expected of Team Leader Choi. He was reliable.

He had obviously thought of a way to overcome this crisis.

After calming the chaos with his composed voice, Team Leader Choi pointed at me.

“Mr. Jin Taekyung here will solve it!”

“…?”

“Mr. Jin Taekyung. What should we do?”

“Why are you asking me?”

“I trust Mr. Jin Taekyung!”

“…”

Why did he trust me?

In a situation like this, believing in God, Buddha, or Allah would probably be more helpful.

I was momentarily speechless as people’s gazes came flying toward me from all sides.

“Come to think of it, I’ve heard about that Hunter. They say he’s so formidable that even Comrade Chairman Xiao Yang made a special request for him.”

“I’ve heard the rumors too. They say he might be a new S-rank Hunter. Apparently, he defeated two named monsters all by himself.”

“Ooh! Ooooooh!”

“We’re saved! We’re going to live!”

- You vile human! I knew you were strong, but you’re beyond my wildest imagination! Rejoice, my legion. Your commander has survived!

“…You’re already dead.”

This was driving me insane. None of them were in their right minds anymore.

I stared at Team Leader Choi in disbelief.

“What exactly are you basing this on?”

He answered without hesitation.

“I told you. I trust you.”

“That’s what I’m asking. Where does that baseless trust come from—”

“It isn’t baseless.”

“What?”

“Your attitude, tone of voice, and expression in a situation like this. All of them are grounds for my trust.”

“…”

Only then did I finally realize it.

I was flustered by the unexpected situation, but I felt no fear or terror whatsoever.

The answer was closer than I had thought.

*Because I’m strong.*

I was strong. Stronger than ever. Strong enough to avoid any danger.

That was why neither the monsters sweeping across the ground like a wave nor the flock of wyverns right behind us frightened me.

“So that’s it…”

I muttered quietly to myself before opening my mouth.

“Who’s the captain?”

A hand shot up from the cockpit ahead.

It was trembling violently. With his other hand, the captain was probably gripping the controls for dear life, desperately trying to evade the wyverns lunging at us.

“I-I am.”

“Can I open the door for a second?”

“What?”

“I said, can I open the plane door?”

The captain must have been so shocked that he poked his head out and stared at me as though I were insane.

“Of course not! Not only is it impossible to open because of the pressure-sealing system, the aircraft will be damaged because it can’t withstand the pressure difference! You won’t even be able to breathe properly!”

Team Leader Choi, fiddling with the ring on his finger, cut in.

“I think I can block the pressure. I don’t know what you have in mind, but go ahead and try.”

“Okay.”

“Don’t! You *bangzi* bastards![^1] Are you trying to kill us all?”

“…What did you just call us?”

The nerve of him, insulting Koreans right in front of a proud Korean kimchi man like me!

Realizing the slip of the tongue that had escaped him, the captain’s face turned pale.

“No, that’s not what I meant.”

“You fucking Chink bastard. Damn it.”

“…”

“Hey, Captain!”

“Y-Yes?”

“I’m opening it.”

“Ah! Ah!”

Before the captain had time to stop me, I opened the door.

No—I cut it open.

Shhk!

Sword qi—the force called an Aura Blade in the modern world—sliced through the sturdy alloy and created a small door.

Just as a Supreme Peak master of the Murim could do, it was a tremendous power that only an S-rank Hunter could display here.

Team Leader Choi’s eyes widened in shock.

“Mr. Jin Taekyung, this is—”

“Team Leader!”

Whoooosh!

This was no time to be surprised. The tremendous wind and pressure were making the aircraft lurch, turning the cabin into a complete mess.

Team Leader Choi came to his senses at the screams and my shout, then rubbed his ring.

“An impenetrable barrier surrounds us. Barrier!”

“Oh.”

Along with the incantation, a transparent membrane of energy sealed off the new opening without leaving so much as a gap.

So there was a way to do this.

With a brief exclamation of admiration, I stuck my upper body out of the cabin.

Because Team Leader Choi’s barrier recognized me as an ally, it let me pass through without resistance.

Rumble, rumble!

The wind pressure slammed into my upper body as though trying to crush me. I grinned.

*This is no joke.*

But it wasn’t unbearable.

Actually, it would have been strange if I couldn’t withstand it. Compared to the waves of qi the Western Heaven Demon Lord had emitted, this was no more than a gentle spring breeze.

- Kyaaaauuu!

The monster’s sharp cry mixed into that spring breeze.

The flock of wyverns had already drawn close enough for me to judge the distance.

*About a hundred meters. I’ve never tried this before, but… at this distance, it should be enough.*

*Open inventory. Equip.*

Ssswish.

A spear I had bought at a discount from the Hunter Market appeared in my hand.

Like a javelin thrower, I drew my shoulder far back. From my waist to my wrist, the necessary muscles and tendons pulled taut like bowstrings.

- Kyaau!

The leading wyvern, their chief, noticed that something was wrong and threw back its head with a shriek.

I could see a pure-white current of air being sucked toward its snout.

*That’s…*

- Breath! It’s using Breath! Dodge it, you vile human!

The Skeleton Warlord was right.

Among the countless monsters, Breath was a power granted only to the dragonkin. Inside the wyvern’s wide-open maw, I could clearly see it taking shape.

Whooooom.

A massive sphere of wind. An air breath capable of shredding metal like paper had formed completely.

“Hey, wyvern!”

- Kya?

“I’m putting it in!”

I shouted like a thunderbolt and whipped my drawn-back shoulder forward.

Fwoom—whooosh!

Fiery concentrated qi sheathed the spearhead, burning the air and cleaving the wind.

The wyvern’s bright yellow eyes widened at the blue-white streak of light shooting straight toward it.

- Kiiiiiik!

Whoooom!

Compressed air burst from the tip of the spear. A cloud of white.

And then—

Thwack! Boom-boom!

A massive body plunged toward the ground like a kite with its string cut.

* * *

- Kyaau?

- Kiiit?

Around a dozen pairs of bright yellow eyes stared at one another.

Wyverns were ferocious creatures from the moment they were born, but at this moment, they were utterly bewildered and had no idea what to do.

- Kikikit?

- Kiiik…

*What? Is the boss dead?*

*Looks that way…*

After exchanging words in their own language, the wyverns were dumbfounded.

Their leader was an exceptionally powerful member of their species—so powerful that he was known as the “Black Star.”

And now, the Black Star had become a black speck falling toward the impossibly distant ground.

- Kiririk?

- Grrrrr.

None of them had even properly seen how he died.

They could only guess that the tiny human had thrown a spear and hit him.

But that was impossible.

How could a mere human dare lay a hand on a descendant of the great dragons…

“Hey, green wyvern over there!”

- Kiiik?

“I’m putting it in!”

Thwack!

This time, they saw it clearly: their companion’s head bursting apart in the beam of light.

- Kiiik!

- Kyaaaauuu!

*Another of our bloodline has died after the boss!*

Furious beyond measure, the wyverns vowed revenge against that damned human.

- Kiiit!

Of course, not today.

They would get their revenge later. A little later.

“Hey, blue wyvern over there!”

Thwack!

*…Will they ever get their revenge?*

Around a dozen pairs of wings began flapping desperately.

[^1]: *Bangzi* (棒子) is a derogatory Chinese slur for Koreans.
```
