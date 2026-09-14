<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0379.txt",
      "sha256": "9ede64f7ec4876ce13f9000aa10c43e1f0849bc2f842b87812931335504058b6",
      "bytes": 13984
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "de5d193ff353322f38cdfd3cfdcbe90afd57babae8e2ef244a6e875c453b3e83",
      "bytes": 7394
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3a4c388c1dfecf3e88bf9fa95abf09b47320a3ef639a08a980c37bc5f4203d66",
      "bytes": 7582
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "62fd3f513133c642d4eabe3cd127fc9f80ffea7a50501f8ecd0a0e6593a0f900",
      "bytes": 4950
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 13107
}
-->

# Durable State Update — Chapter 379

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 379. Keep at most
2 continuity_sources. Use only chapter
numbers through 379. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 379,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 379,
    "continuity_sources": [379],
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
    "Taekyung has successfully completed Logout and returned to the modern world aboard a private jet sent by China's Central Committee toward Chengdu International Airport.",
    "Cheongpung is Mimi's temporary guardian while the Tang Clan's future is uncertain.",
    "The Divine Physician, referred to in Taekyung's joke as Dongbong, has asked Taekyung for time before his departure; the request remains undisclosed.",
    "Dongbong predicts that a great war will soon occur and asks Mungyeong to prevent it as the Divine Physician; Mungyeong verbally refuses and says the Murim is not where he belongs, while the announced departure from Chengdu's western port remains unresolved.",
    "Taekyung and Cheongpung were preparing to leave Sichuan by fast ship from Chengdu's western port after the Hour of the Dog.",
    "Mu Song is the boatman associated with the water bandits preparing the ship.",
    "An unidentified boy reaches the port immediately before departure and is accepted as one more passenger.",
    "The Sichuan Governor's favorite concubine Ae-hyang manipulated him into concealing the government uniforms and weapons involved in the recent martial-artist conflict and preparing a false memorial that exaggerates his role in restoring order. A sinister red light entered her eyes, and she appears to serve an unidentified superior.",
    "Chengdu International Airport is under attack by monsters, with humans and monsters fighting on the ground while around a dozen A-rank wyverns pursue Taekyung's private jet.",
    "Taekyung concludes that the Lich, the supreme undead monster associated with the recent monster wave, has extended its reach to Chengdu.",
    "Team Leader Choi accompanies Taekyung, trusts him to resolve the attack, and can create a pressure-blocking barrier with a ring.",
    "Taekyung cuts an opening in the aircraft with sword qi, called an Aura Blade in the modern world, and kills the lead wyvern and multiple others with a spear."
  ],
  "continuity_sources": [
    378
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
    "The Lich's exact role in the Chengdu attack and the extent of its reach remain unresolved.",
    "Whether Taekyung's private jet survives the ongoing wyvern attack remains unresolved."
  ],
  "safe_through": 378,
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
    "Render 흑룡갑 as Black Dragon Armor, 화룡갑 as Flame Dragon Armor, 수룡채 as Water Dragon Stronghold, 열화신공 as Blazing Flame Divine Art, 상산왕 as King of Shangshan, and 삼공 as Grand Councilor.",
    "Render 최 팀장 as Team Leader Choi, 리치 as Lich, 스켈레톤 워로드 as Skeleton Warlord, 샤오 양 as Xiao Yang, 중국 중앙위원회 as Central Committee of China, 쓰촨성 as Sichuan Province, 청두 국제공항 as Chengdu International Airport, 헌터 마켓 as Hunter Market, and 검은 별 as Black Star.",
    "Render 와이번 as wyvern, 드레이크 as drake, 용족 as dragonkin, 브레스 as Breath, 강기 as sword qi, and 오라 블레이드 as Aura Blade.",
    "Retain a footnote explaining 빵즈 as a derogatory Chinese slur for Koreans."
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
| 최 팀장 | **Team Leader Choi** | Taekyung's modern-world team leader aboard the private jet. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 스켈레톤 워로드 | **Skeleton Warlord** | Undead commander accompanying Taekyung's group. |
| 샤오 양 | **Xiao Yang** | Chairman credited by passengers with making a special request for Taekyung. |
| 중국 중앙위원회 | **Central Committee of China** | Organization that sent the private jet. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 청두 국제공항 | **Chengdu International Airport** | Destination airport under attack. |
| 헌터 마켓 | **Hunter Market** | Market where Taekyung bought the spear at a discount. |
| 검은 별 | **Black Star** | Epithet of the exceptionally powerful lead wyvern. |

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
| 진태경 | 최 팀장 | subordinate_to_team_leader | Team Leader | polite-but-direct | Taekyung uses 팀장님 while asking Choi for help and addressing him during the crisis. |
| 최 팀장 | 진태경 | team_leader_to_trusted_hunter | Mr. Jin Taekyung | professional-deferential | Choi repeatedly uses 진태경 씨 while relying on Taekyung to resolve the attack. |
| 진태경 | 기장 | passenger_to_captain | Captain | casual-urgent | Taekyung directly asks the captain for permission before cutting open the aircraft door. |

## Exact glossary matches

| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |

## Listed compact profiles

(No chapter-safe profiles matched.)

## Korean source

```text
＃379화



드드드득!

거대한 울림과 지면을 통해 전해지는 진동.

지평선을 바라본 스무 살의 청년. 샤오 쉔(Shao Shen)은 도무지 지금의 상황을 믿을 수 없었다.

‘수천 킬로 밖에 있어야 할 몬스터들이 어떻게……!’

이것은 샤오 쉔 혼자만이 떠올린 의문이 아니었다.

천여 명의 공안 무력부 소속의 헌터와 치안 유지를 위해 파견된 오천 명의 중국 인민 해방군. 청두 국제공항에 주둔해 있던 모두가 같은 의문을 떠올렸고, 눈앞에 닥쳐 온 현실에 경악했다.

- 취이익!

- 그워어어!

하급 몬스터인 고블린, 오크부터 트롤, 오우거와 라이칸슬로프 같은 상위 몬스터까지.

지평선을 가득 메운 몬스터 대군이 괴성과 함께 돌진하고 있었다.

1km의 거리가 시시각각 빠르게 좁혀지는 광경에 비명 같은 외침이 터져 나왔다.

“각 제대 별로 대열 갖춰! 집합! 집하압-!”

“쏴, 쏴라! 쏘란 말이다!”

타다다당! 꽈앙!

황급히 대열을 갖춘 인민해방군이 상관의 명령에 따라 화력을 퍼부었지만, 효과는 미비하기 짝이 없었다.

예상치 못한 몬스터 대군의 습격.

아무 능력도 없는 일반인에 불과한 군인들은 공포로 몸이 굳었고, 그들이 발사한 화기는 고작해야 하급 몬스터들에게만 통하는 수준이었다.

“몬스터들이, 몬스터들이 너무 많습니다!”

“파일럿!”

“어서 전투기를 띄워라! 놈들의 머리 위로 폭격을……!”

다급한 지휘관들의 외침은, 다음 순간 하늘 위에서 울려 퍼진 흉포한 괴성에 파묻혔다.

- 캬우우우우!

“저, 저건!”

“와이번! 와이번이다!”

석양을 등지고 날아오는 거대한 동체.

창공의 공포라 불리는 와이번을 선두로 수십 마리의 그리폰(Griffon), 가고일(Gargoyle)이 뒤따른다.

수 미터의 날개를 비스듬히 꺾으며 하강한 A급 몬스터들이 아직 미처 이륙하지 못한 전투기들을 덮쳤다.

콰드드득! 콰광!

위력적인 날갯짓에 수 톤의 쇳덩이가 들썩였고, 마력이 실린 발톱에 전투기의 기체가 종잇장처럼 찢겨 나갔다.

폭발과 함께 엄청난 힘으로 튕겨 나간 금속 파편이 황급히 뛰어가던 파일럿들을 덮쳤다.

퍼버벙! 콰직!

비명조차 남기지 못한 즉사.

정신을 차린 지휘관의 명령에 따라 총기가 불을 뿜었지만, 강력한 마력을 머금은 피부와 가죽은 수백, 수천 발의 탄환으로도 생채기만 내는 것이 고작이었다.

- 키키키킷.

무력한 인간을 비웃는 몬스터의 웃음소리에, 사람들은 전신의 털이 곤두서는 듯한 충격과 공포를 느꼈다.

“이, 이럴 수가.”

지상과 상공을 가득 메운 몬스터 대군. 화기조차 제대로 통하지 않는 놈들은 그야말로 괴물이었다.

“괴, 괴물…….”

“나, 난 살아야겠어. 이런 곳에서 개죽음당하기는 싫다고!”

죽음에 대한 공포는 그 어떤 전염병보다 빠르게 퍼져 나갔다.

인민 해방군이 하나둘씩 뒷걸음질 치던 그때, 오히려 앞을 향해 나아가는 한 사람이 있었다.

“물러서지 마라!”

아직 앳된 기가 가시지 않은 청년, 샤오 쉔이 타오르는 눈빛으로 외쳤다.

그가 착용한 갑옷의 가슴팍에는 중화인민공화국의 국기인 오성홍기(五星紅旗)가 새겨져 있었다.

“우리가 누구인가!”

젊은 청년의 물음에 도망치려던 이들이 발걸음을 멈췄다.

샤오 쉔은 수백 미터 밖에서 돌격해 오는 몬스터 군단을 노려보았다. 깊게 눌러쓴 투구 사이로 다시 한번 천둥 같은 목소리가 터져 나왔다.

“우리가 누구인가!”

피가 끓어오르는 듯한 외침.

모두의 시선 속에 샤오 쉔은 창날을 곧추세웠다.

“우리는 중화의 후예이고, 인민 해방군과 공안 무력부(公安武力部)의 형제들이다!”

하늘을 찌를 듯 높이 솟구친 창날에서 석양빛을 닮은 오라가 솟구쳤다.

츠츠츠츠!

“가자! 저 괴물들을 모조리 쓸어 버리자!”

“와아아아아!”

귀가 먹먹해지는 거대한 함성이 지축을 뒤흔들었다.

샤오 쉔을 필두로, 공안 무력부 소속의 헌터들이 각자의 무기를 손에 쥔 채 몬스터 대군을 향해 맹호처럼 짓쳐 들었다.

“물러서지 마라! 중화의 힘을 보여 줘라!”

“으아아아!”

- 구워어어어!

- 아우우우!

죽음을 각오한 결의가 담긴 인간의 외침과 몬스터들의 괴성이 뒤섞인다. 한 덩어리가 된 두 집단이 서로를 향해 얽혀들었다.

콰과과과광!

하늘과 땅을 울리는 격돌. 그리고 사방에서 빗발치는 죽음.

“크아아악!”

- 쿠에엑!

푸푸푹! 퍼걱!!

지상 곳곳에서 비명과 굉음이 울려 퍼졌다.

오라가 서린 A급 헌터의 검신이 라이칸스로프의 목을 갈랐고, 오우거가 휘두른 쇠몽둥이에 서너 명의 헌터들이 피곤죽이 되어 날아간다.

힘을 합쳐 몬스터 하나를 쓰러트리고 다음 적을 향해 무기를 휘두르려던 두 헌터의 머리 위에 거대한 그림자가 드리웠다.

- 키이이잇!

서걱!

급강하한 그리폰의 발톱이 헌터들의 육신을 갑옷과 함께 갈기갈기 찢었다.

다음 사냥감을 찾아 헤매는 그리폰을 향해 커다란 불의 구(球)가 날아왔다.

“파이어 볼(Fire Ball)!”

퍼버벙!

매캐한 연기와 함께 상공을 유영하던 그리폰의 동체가 휘청였다. 지상에서 호시탐탐 때를 노리고 있던 원거리 부대는 그 틈을 놓치지 않았다.

“지금!”

펑! 퍼버버벅!

가지각색의 마법과 마나를 한껏 머금은 화살이 그리폰을 꿰뚫었다.

단말마와 함께 추락하는 그리폰의 모습에 비행 몬스터들이 흉포한 괴성을 토해 냈다.

- 캬우우우우!

원거리 부대를 향해 내리꽂히는 비행 몬스터들을 가로막은 것은, 납과 철로 이루어진 현대식 무기였다.

“일제 사격, 실시!”

타타타타탕! 콰앙!

무수히 많은 소총과 중화기. 수십여 대의 전차가 일시에 불을 토해냈다.

비록 몬스터들의 마력과 상극이라 할 수 있는 마나(Mana)의 힘에 비할 바는 아니지만, 일거에 화력을 집중시키니 비행 몬스터들도 주춤할 수밖에 없었다.

- 키잇!

“통한다!”

“다른 곳은 소용없다! 눈을 노려!”

날 때부터 마력을 머금은 몬스터들의 피륙은 대부분의 물리력을 가뿐히 무시한다. 그러나 단 한 곳, 눈만은 예외였다.

얕은 피막에 싸여 있는 안구는 중화기를 동원한다면 충분히 피해를 입힐 수 있는 수준.

멈칫거리는 몬스터들의 모습에, 모든 광경을 지켜보고 있던 사단장이 신나게 지휘봉을 휘둘렀다.

“더! 더 퍼부어라! 저 괴물들이 꼼짝도 못 하게…….”

콰아아아아!

음성은 이어지지 못했다.

그린 와이번이 쏘아 보낸 포이즌 브레스(Poison Breath)가 반경 백여 미터를 뒤덮었고, 사단장을 포함한 참모 지휘부는 강력한 산성 독을 뒤집어쓴 채 녹아내렸다.

“사, 사단장님!”

“지휘부가……!”

눈 깜짝할 사이에 수백의 병사와 고급 지휘관을 잃은 인민 해방군은 패닉 상태에 빠졌다.

장교와 부사관, 병사. 가릴 것 없이 모두가 경악에 찬 외침과 함께 눈 앞에 펼쳐진 끔찍한 광경을 바라봤다.

“이럴 수가…….”

“이, 이건 아니야. 이럴 수는 없어! 이런 건 내 임무가 아니라고!”

누군가의 비명은 모두의 심정을 대변하는 것이었다.

만일을 대비해 전력을 끌고 오긴 했지만, 그들의 주 임무는 곧 청두 국제공항에 도착할 외국의 헌터들과 합류, 호위하며 상부의 명령에 따라 움직이는 것이었다.

수천 킬로미터 밖에 있을 몬스터 군단이 쳐들어올 거라는 내용은 어디에서도 들은 바 없었다.

“이게 도대체…….”

“죽는다. 우리 모두 죽을 거야.”

잠시 잊었던 공포감이 인민 해방군의 머리 위에 내려앉았다.

그들은 전장의 선두에서 싸우고 있는 공안 무력부의 헌터들이 아니라, 현대식 화기를 든 평범한 일반인에 불과했으니까.

그리고 불길한 짐작은 곧 현실이 되었다. 그들이 생각했던 것보다 더한 악몽으로.

- 옴. 느. 하. 소. 유.

뚝뚝 끊어지는 목소리. 수신이 불안정한 라디오의 노이즈를 닮은 스산한 소음이 전장에 울려 퍼진다.

어디선가 몰려온 검은 안개가 사람들의 머리 위를 뒤덮었다.

- 옌. 위. 가. 지. 케!

그때였다. 끔찍한 변화가 일어난 것은.

쏴아아아악!

먹구름처럼 어두운 마력이 피와 시체를 타고 거미줄처럼 뻗어 나갔다.

싸늘하게 식어 가는 시신에 새로운 힘과 영혼을 불어넣고, 사슬로 묶어 종속시킨다.

투둑, 투두두둑.

새로운 생명을 얻고 죽음의 웅덩이에서 서서히 몸을 일으키는 백골(白骨)의 군단.

무수한 망자들을 보이지 않는 사슬로 엮어 종으로 삼은 ‘그 존재들’은 만족스럽게 웃었다.

- 킥, 키키킥.

- 그극. 키히히.



* * *



- 그르르륵.

끓어오르는 소리와 함께 사내가 몸을 일으킨다.

오성홍기가 새겨진 갑옷과 거대한 도끼를 든 그는 샤오 쉔이 기억하는 A급 헌터의 모습 그대로였다.

‘……야오위 씨.’

그러나 샤오 쉔은 사내의 이름을 소리 내어 부를 수 없었고, 부르지도 못했다.

눈앞의 그가, 더이상 자신이 알던 사람이 아니라는 사실을 알기 때문이다.

‘아, 아아.’

만약 십여 분 전 그가 목이 잘리는 광경을 목격하지 않았다면, 지금 이 순간 자신의 잘려 나간 목을 옆구리에 낀 채 일어나지 않았다면 샤오 쉔은 그를 동료이자 친구로 생각했을 것이다.

하지만 이제 야오위는 존재하지 않는다. 샤오 쉔의 입술 사이에서 그의 새로운 이름이 흘러나왔다.

“듀라한(Dullahan)…….”

목 없는 기사. 듀라한.

샤오 쉔은 상위 언데드 몬스터로 거듭난 동료의 모습에 입술을 깨물었다. 뜨거운 무언가가 볼을 타고 흘러내렸다.

“미안합니다. 정말로.”

- 그어어어!

괴성과 함께 달려드는 듀라한을 향해, 샤오 쉔은 바람처럼 쏘아졌다.

과거 두 사람은 종종 이렇게 대련을 벌이고는 했다. 단순한 호승심으로 시작한 대련은 매일마다 계속되었고, 대련이 끝나면 야오위의 투정을 받아 주어야 했다.



‘어린놈이 예의가 없어요, 예의가. 한 번 져 주면 덧나냐?’

‘하하. 밥이나 먹으러 가죠. 대련에 진 사람이 계산하기로 했으니까, 오늘도 야오위 씨가 사겠네요.’

‘집에 돈도 많은 놈이 밝히기는. 내가 언젠가 네 녀석한테 밥 얻어먹고 만다.’



하지만 그런 일은 과거에도, 앞으로도 없을 것이다. 승자는 늘 샤오 쉔이었다.

‘잘 가요. 그동안 고마웠습니다.’

후웅! 서걱!

휘둘러진 도끼는 허공을 갈랐고, 샤오 쉔의 창날에서 솟구친 오러는 듀라한의 상반신을 갈랐다.

허리춤으로부터 그어진 선. 목 없는 기사의 신형이 천천히 허물어진다.

쿵, 털썩.

쓰러진 듀라한, 아니 야오위의 얼굴을 물끄러미 내려다보던 샤오 쉔의 눈동자가 뜨겁게 달아올랐다.

“감히, 감히 이런 짓을…….”

반나절 전만 해도 함께 웃고 떠들던 친구와 동료들이 언데드 몬스터가 되었다.

공안 무력부의 헌터들은 군기가 엄정하기로 이름 높지만 피 한 방울 없는 냉혈한들은 아니었다.

죽을 각오로 전투에 임하던 헌터들은 처음으로 인정(人情)이라는 두려움에 직면했다.

“정신 차려! 나 류인친이야! 류인친!”

“혀, 형……!”

- 크르르륵!

퍼걱! 콰과광!

사방에서 비명과 죽음이 빗발쳤다. 절반에 가까운 피해를 입은 공안 무력부와 달리, 오히려 숫자를 불린 몬스터 군단은 끊임없이 밀려들었다.

‘이곳에서, 이렇게 죽는 건가?’

샤오 쉔은 난생처음으로 죽음을 떠올렸다. 늘 밝고 쾌활하던 그가 이렇게 생각할 만큼 상황은 절망적이었다.

‘위험 신호를 받지 못했으니 아마도 통신은 불통, 지원도 없을 테니…… 정말 끝장이구나.’

서걱!

달려드는 언데드 몬스터를 연달아 베어 넘긴 샤오 쉔은 허탈하게 웃으며 하늘을 바라봤다.

노을빛이 퍽 아름답다. 곧 해가 지고 어둠이 찾아오면, 이런 광경도 두 번 다시 보지 못할 것이다.

‘다행이야. 마지막으로 보는 하늘치고는 썩 괜찮…….’

어?

샤오 쉔은 생각을 잇지 못하고 눈을 깜빡였다.

하늘 위, 엄청나게 거대한 무언가가 빠른 속도로 전장을 향해 가까워지고 있었다.

‘비행기?’

콰아아아아아!

불길이 타오르는 거대한 기체. 그리고 드넓은 창공에 울려퍼지는 누군가의 외침.

“야아! 몬스터어!”

“……?”

- ……?

지금 헛것을 들은 건가.

샤오 쉔뿐만 아니라 전장의 모두가 하늘을 올려다보았다.

광기마저 느껴지는 누군가의 목소리가 천둥처럼 울려 퍼졌다.

“박는다!”

박아? 뭘?

샤오 쉔은 곧 그 말의 뜻을 깨달을 수 있었다.

쿠구구구궁!

비행기의 거대한 동체가, 그대로 전장을 휩쓸었다.
```

## Final English reading copy

```markdown
# Chapter 379

Rrrrrumble!

A tremendous roar, followed by vibrations traveling through the ground.

Shao Shen, a twenty-year-old young man staring toward the horizon, simply could not believe what he was seeing.

*How can monsters that should be thousands of kilometers away be here…?*

He was not the only one asking that question.

More than a thousand Hunters from the Public Security Armed Forces, along with five thousand soldiers of the Chinese People’s Liberation Army dispatched to maintain public order—all of them stationed at Chengdu International Airport—were asking themselves the same thing as they stared in horror at the reality bearing down on them.

- Ssssss!

- Grrrrr!

From low-level monsters like goblins and orcs to higher monsters like trolls, ogres, and lycanthropes—

A monster army filling the horizon was charging forward with hideous roars.

The distance of one kilometer was shrinking by the second. Shouts like screams erupted across the airport.

“Form ranks by unit! Assemble! Assembllllle—!”

“Fire! Fire! I said fire!”

Rat-a-tat-tat! Boom!

The People’s Liberation Army hurriedly formed ranks and poured out firepower at their commanders’ orders, but the effect was pitifully small.

They had been ambushed by an unexpected monster army.

The soldiers, who were merely ordinary people without any abilities, froze in fear. Their firearms were barely effective against the low-level monsters at best.

“There are too many monsters! There are too many!”

“Pilots!”

“Get the fighter jets into the air! Bomb them from above—!”

The desperate shouts of the commanders were drowned out the next moment by a savage roar that rang across the sky.

- Kyaaaauuu!

“W-What is that?”

“Wyverns! They’re wyverns!”

A massive body came flying with the setting sun behind it.

Leading the charge were wyverns, known as the terror of the skies, followed by dozens of griffons and gargoyles.

The A-rank monsters descended with their wings angled sharply, swooping down upon the fighter jets that had not yet managed to take off.

Krrrunch! Boom!

The powerful beat of their wings made several-ton blocks of metal jolt, while claws infused with magic tore through the fighter jets like sheets of paper.

The metal fragments hurled away by the explosions crashed into the pilots running frantically across the tarmac.

Bang-bang! Crunch!

Instant death. They did not even have time to scream.

The guns began spitting fire at the commanders’ orders once they regained their senses, but the flesh and hide saturated with powerful magic could do little more than suffer scratches from hundreds or even thousands of bullets.

- Kikikikit.

The monsters laughed at the helpless humans.

Everyone felt a shock and terror that made the hair all over their bodies stand on end.

“H-How can this be?”

A monster army filled the ground and the sky. The creatures that could barely be harmed by firearms were monsters in the truest sense.

“M-Monsters…”

“I-I have to live. I don’t want to die like a dog in a place like this!”

Fear of death spread faster than any epidemic.

And just as the soldiers of the People’s Liberation Army began taking a step backward one by one, one person instead moved forward.

“Don’t retreat!”

Shao Shen, a young man whose boyishness had not yet faded, shouted with blazing eyes.

The five-star red flag of the People’s Republic of China was embroidered across the chest of his armor.

“Who are we?”

At the young man’s question, those who had been about to flee stopped in their tracks.

Shao Shen glared at the monster army charging from several hundred meters away. His thunderous voice erupted again from beneath his tightly pulled helmet.

“Who are we?”

His shout made their blood seem to boil.

With everyone watching him, Shao Shen raised his spear point straight into the air.

“We are the descendants of Zhonghua, and we are brothers of the People’s Liberation Army and the Public Security Armed Forces!”

An aura resembling the colors of the setting sun surged from the spear point, which rose high enough to pierce the sky.

Ssssss!

“Let’s go! Let’s sweep away every last one of those monsters!”

“Waaaaah!”

A colossal roar that made their ears ring shook the earth.

Led by Shao Shen, the Hunters of the Public Security Armed Forces gripped their weapons and charged into the monster army like fierce tigers.

“Don’t retreat! Show them the power of Zhonghua!”

“Uraaaaaah!”

- Grrrrr!

- Awooooo!

Human cries filled with the resolve to face death mingled with the monsters’ roars.

The two groups became one mass as they crashed into each other.

Kra-kra-kra-boom!

A clash that shook the heavens and earth.

And death raining down from every direction.

“Gaaaaah!”

- Kweeeek!

Thud! Crunch!

Screams and thunderous impacts rang out across the battlefield.

The aura-coated blade of an A-rank Hunter cleaved through a lycanthrope’s neck, while an ogre’s iron club sent three or four Hunters flying as bloody pulp.

Two Hunters worked together to bring down a monster, then raised their weapons toward the next enemy.

A massive shadow fell over their heads.

- Kiiiiit!

Slash!

The claws of a griffon diving from the sky shredded the Hunters’ bodies along with their armor.

A large ball of fire flew toward the griffon as it searched for its next prey.

“Fireball!”

Bang!

The griffon’s body, gliding through the sky, staggered amid a cloud of acrid smoke.

The ranged units waiting on the ground for their chance did not miss the opening.

“Now!”

Boom! Bang-bang-bang!

Spells of every kind and arrows saturated with mana tore into the griffon.

The flying monsters let out savage cries at the sight of the griffon plummeting with a final scream.

- Kyaaaauuu!

The modern weapons made of lead and iron blocked the flying monsters diving toward the ranged units.

“Commence mass fire!”

Rat-a-tat-tat-tat! Boom!

Countless rifles and heavy weapons fired at once. Dozens of tanks spewed fire simultaneously.

Though modern weapons were no match for mana—the natural counter to monsters’ magic—concentrating all that firepower at once still forced even the flying monsters to falter.

- Kiiit!

“It works!”

“It’s useless anywhere else! Aim for their eyes!”

Monsters were born with magic running through their bodies, and their flesh could casually ignore most physical force.

But their eyes were the one exception.

Their eyeballs, covered only by a thin membrane, could be damaged if heavy weapons were brought to bear.

At the sight of the monsters hesitating, the division commander watching everything unfold excitedly waved his baton.

“More! Pour more fire into them! Don’t let those monsters move an inch—”

Whoooooom!

His voice never finished.

Poison Breath fired by a green wyvern covered a radius of more than a hundred meters. The division commander and the command staff were drenched in potent acidic poison and melted away.

“D-Division Commander!”

“The command staff…!”

The People’s Liberation Army fell into a state of panic after losing hundreds of soldiers and senior commanders in the blink of an eye.

Officers, noncommissioned officers, and soldiers alike stared at the horrific scene unfolding before them, crying out in shock.

“This can’t be happening…”

“N-No. This isn’t right. This can’t be happening! This isn’t what I signed up for!”

Someone’s scream spoke for everyone.

They had brought their forces as a precaution, but their primary mission was to join up with and escort the foreign Hunters who would soon arrive at Chengdu International Airport, then follow orders from above.

They had never heard anything about a monster army that should have been thousands of kilometers away invading the airport.

“What the hell is going on…?”

“We’re going to die. We’re all going to die.”

The fear they had briefly forgotten settled over the heads of the People’s Liberation Army once more.

Unlike the Hunters of the Public Security Armed Forces fighting on the front lines, they were merely ordinary people carrying modern firearms.

And their ominous premonition soon became reality.

A nightmare far worse than they had imagined.

- Om. Ne. Ha. So. Yu.

A voice broken into disconnected syllables.

An eerie noise resembling the static of a radio with an unstable signal echoed across the battlefield.

Black fog that had come from somewhere spread over the heads of the people.

- Yen. Wi. Ga. Ji. Ke!

That was when the horrifying change occurred.

Swoooooosh!

Dark magic as black as storm clouds spread like a web through the blood and corpses.

It breathed new strength and souls into bodies that were growing cold, then bound them in chains and enslaved them.

Snap. Snap-snap.

Given new life, an army of skeletons slowly rose from the pools of death.

*Those beings* had woven countless dead together with invisible chains and made them their slaves.

They laughed in satisfaction.

- Kik, kikikik.

- Grrk. Kihihihi.

* * *

- Grrrrr.

With a bubbling sound, a man rose to his feet.

He wore armor bearing the five-star red flag and carried a massive ax. He looked exactly like the A-rank Hunter Shao Shen remembered.

*…Mr. Yao Wei.*

But Shao Shen could not call the man’s name aloud.

No—he could not bring himself to call it.

He knew that the person standing before him was no longer the man he had known.

*Ah… ahhh.*

If Shao Shen had not witnessed the man’s decapitation ten minutes earlier, if he had not seen him rise with his severed head tucked beneath his arm, Shao Shen would have thought of him as a comrade and friend.

But Yao Wei no longer existed.

A new name slipped between Shao Shen’s lips.

“Dullahan…”

A headless knight.

A dullahan.

Shao Shen bit his lip at the sight of his comrade transformed into a higher undead monster.

Something hot ran down his cheek.

“I’m sorry. I really am.”

- Grrrrraaaah!

As the dullahan charged at him with a roar, Shao Shen shot forward like the wind.

In the past, the two of them had often sparred like this.

Their bouts had begun with nothing more than competitive pride and continued day after day. Once each spar ended, Shao Shen had to put up with Yao Wei’s complaints.



*You little brat have no manners, I tell you. Would it kill you to let me win once?*

*Ha-ha. Let’s go get something to eat. The loser was supposed to pay, so I guess you’re buying again today, Mr. Yao Wei.*

*You’ve got plenty of money at home, and you’re still so cheap. One day, I’ll make you buy me a meal.*



But that had never happened before, and now it never would. Shao Shen had always been the winner.

*Goodbye. Thank you for everything.*

Whoosh! Slash!

The ax swept through empty air, while the aura surging from Shao Shen’s spear point cleaved through the dullahan’s upper body.

A cut line appeared, starting at his waist. The headless knight’s body slowly crumpled.

Thud. Collapse.

Shao Shen stared blankly down at the face of the fallen dullahan—no, Yao Wei.

His eyes burned.

“How dare you… How dare you do this…”

His friends and comrades, who had been laughing and joking with him only half a day earlier, had become undead monsters.

The Hunters of the Public Security Armed Forces were famous for their strict discipline, but they were not cold-blooded people without a drop of human feeling.

The Hunters who had entered the battle prepared to die now faced something frightening for the first time—the fear of human attachment.

“Wake up! It’s me, Ryu Inchin! Ryu Inchin!”

“H-Hyung…!”

- Grrrrr!

Crunch! Boom!

Screams and death rained down from every direction.

Unlike the Public Security Armed Forces, which had suffered casualties approaching half its strength, the monster army had increased its numbers and continued to surge forward without end.

*Am I going to die here, like this?*

For the first time in his life, Shao Shen thought about death.

The situation was so desperate that even someone as bright and cheerful as him had begun to think that way.

*We didn’t receive any warning signal, so communications must be down. There won’t be any reinforcements either… This really is the end.*

Slash!

After cutting down one undead monster after another, Shao Shen laughed hollowly and looked up at the sky.

The sunset was surprisingly beautiful.

When the sun went down and darkness arrived, he would never see a sight like this again.

*It’s not so bad for the last sky I’ll ever see…*

Huh?

Shao Shen blinked, unable to finish the thought.

Something unimaginably enormous was rapidly approaching the battlefield from high above.

*An airplane?*

Whoooooom!

A massive aircraft engulfed in flames.

And someone’s shout rang across the vast sky.

“Hey! Monsters!”

“…?”

- …?

*Am I hearing things?*

Shao Shen was not the only one to look up.

Everyone on the battlefield raised their eyes toward the sky.

A voice that seemed to hold even a hint of madness thundered across the battlefield.

“I’m going to ram it!”

*Ram what?*

Shao Shen soon understood what the voice meant.

Rrrrrumble!

The massive fuselage of the airplane swept across the battlefield.
```
