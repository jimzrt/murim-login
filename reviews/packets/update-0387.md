<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0387.txt",
      "sha256": "027b3f02abdb7e83b2ae6bb9cd2f61b9ba8132439e2cf03e0283c76757518183",
      "bytes": 13996
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "36c1e12203d6e7b113697b89bdcef100356e0dc0c3468514a972d16df93087a5",
      "bytes": 5078
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f4353b294e65128ec1033ee5ed79bd9fac9641f5dd2b18f446b0c29d3aa9320d",
      "bytes": 12980
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "f145ebaadc67c449824ad78c08d093a32859bad389ccea74e84dbaf6557c9cbc",
      "bytes": 509
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "82c367c05865fc5bd01e69f5fccece18cf448e7999eb7a4315465b61620ff2e2",
      "bytes": 9224
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 15452
}
-->

# Durable State Update — Chapter 387

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 387. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 387. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 387,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 387,
    "continuity_sources": [387],
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
    "Jin Taekyung is a Supreme Peak martial artist who has crossed the wall; his exact current level, Fame, complete Titles, martial-art stages, and unassigned points remain unstated.",
    "Taekyung has returned to the modern world and is working with Chinese authorities to stop the monster disaster while seeking Lei Fei and the missing Sichuan Hunters.",
    "Sichuan Province remains in a wartime state, and the current monster wave began in Gaoping District, Nanchong City, after a sudden mana surge.",
    "Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission, and he raised his missing nephew Lei Fei as his own son.",
    "Xiao Yang is Chairman of the Central Military Commission of the Chinese Communist Party, General Secretary, and state chairman of the People's Republic of China.",
    "Xiao Yang has asked the assembled Hunters to prioritize human lives and stop the disaster, while taking personal responsibility and retaining full authority.",
    "Team Leader Choi accompanies Taekyung and continues to trust him during the Chinese crisis.",
    "Magic Johnson is an S-rank Hunter, one of three Archmages worldwide, and a combat-specialized War Mage.",
    "Pai Chen is an S-rank Hunter, Great Cataclysm hero, and former romance-film actress who appears much younger than her actual age.",
    "Wu Heixing is an S-rank Hunter known for heavy media exposure, anti-Korean hostility, and drug and sexual-assault scandals; he is rumored to be the son of a senior Communist Party official.",
    "Prince Felix Alexander Louis is a British prince, third in line to the throne, and holds multiple senior British titles; William serves as his formal attendant.",
    "The Sichuan Tang Clan was devastated by Dark Heaven, owes Taekyung's group a debt, and is considering relocation.",
    "The Chengdu International Airport attack involved an undead army controlled by three incomplete Arch Liches, all of whom Taekyung destroyed.",
    "The Skeleton Warlord absorbed the death energy of the remaining two Arch Liches and became much stronger, but the persistence and full extent of that increase remain unknown.",
    "Dark Heaven's agents, purpose, and connection to the hidden transport formation remain unresolved.",
    "Ae-hyang appears to serve an unidentified superior after a sinister red light entered her eyes, and the Sichuan Governor's false memorial remains unresolved.",
    "Lei Fei's fate and the fate of the Public Security Armed Forces Hunters who disappeared with him remain unresolved.",
    "Lee Jungryong is the practical leader of Ares Guild and one of the world's top three S-rank Hunters; he recognizes Choi Minwoo's growth and that Jin Taekyung has crossed the wall.",
    "The six S-rank Hunters at the temporary headquarters are assigned to six fronts, each supported by three Army and Air Force divisions and Public Security Armed Forces Hunters."
  ],
  "continuity_sources": [
    386
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "Lee Jungryong's purpose beyond attending the bunker meeting, the outcome of Wu Heixing's interrupted attempt to draw his sword, and the identity and request of the person who used Sound Transmission remain unresolved."
  ],
  "safe_through": 386,
  "temporary_decisions": [
    "Use the current Korean source as authoritative; the skipped range is not accepted English continuity.",
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생 and Comrade Chairman for 주석 동지.",
    "Render 반도의 빵즈 as peninsula bangzi and retain the derogatory-slur footnote.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's offensive insult exchange.",
    "Render Pai Chen, Wu Heixing, Prince Felix Alexander Louis, William, Senior General Liao, the Princelings, and the Shanghai clique consistently."
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
| 샤오 쉔 | **Shao Shen** | Twenty-year-old spear-wielding Hunter of the Public Security Armed Forces. |
| 야오위 | **Yao Wei** | A-rank Hunter, Shao Shen's friend and comrade. |
| 류인친 | **Ryu Inchin** | Named combatant of the Public Security Armed Forces; exact relationship to the person calling him hyung is unresolved. |
| 공안 무력부 | **Public Security Armed Forces** | Chinese Hunter organization. |
| 인민 해방군 | **People's Liberation Army** | Chinese military force stationed at the airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 오성홍기 | **Five-Star Red Flag** | National flag of the People's Republic of China. |
| 듀라한 | **Dullahan** | Higher undead monster form taken by Yao Wei. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 중앙 군사 위원회 | **Central Military Commission** | Chinese military body Shao Shen assumes dispatched the unknown S-rank Hunter. |
| 화염신장 | **Flame Divine Palm** | Named fire-based palm technique used by Taekyung. |
| 멸염신권 | **Flame-Annihilating Divine Fist** | Named fire-based fist technique used by Taekyung. |
| 염화일로 | **Flamefire Path** | Named fire-based movement technique used by Jin Taekyung. |
| 아크 리치 | **Arch Lich** | Superior undead being referenced by the three incomplete Liches. |
| 스켈레톤 메이지 | **Skeleton Mage** | Undead unit the three beings consider deploying. |
| 데스나이트 | **Death Knight** | Powerful undead being the three beings plan but fail to create. |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 언데드 헌터 | **Undead Hunter** | Title acquired by Jin Taekyung as the Unexpected Assault Quest Reward. |
| 죽음의 강 | **River of Death** | River upon which the undead swear binding oaths. |
| 검은 숲 | **Black Forest** | Domain the Skeleton Warlord claims to rule. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |
| 오르페우스 폰 막시무스 발렌시아 바이엘른 | **Orpheus von Maximus Valencia Bayern** | Self-styled name used by one of the three undead beings; retains the source's humorous wordplay. |
| 레이페이 | **Lei Fei** | Previously undisclosed Chinese S-rank Hunter and commander of the Sichuan Public Security Armed Forces; missing with his Hunters. |
| 난충시 | **Nanchong City** | City containing Gaoping District, where the monster wave began. |
| 가오핑구 | **Gaoping District** | District in Nanchong City where the first monster-wave signs appeared. |
| 청성산 | **Mount Qingcheng** | Mountain containing the temporary operations headquarters. |
| 핑핑이 | **Pingping** | Taekyung's joking guess at the name of the deceased former chairman; not established as the actual name. |
| 팽팽이 | **Pengpeng** | Taekyung's joking alternative guess at the name of the deceased former chairman; not established as the actual name. |
| 매직 존슨 | **Magic Johnson** | S-rank Hunter, one of the three Archmages, and a combat-specialized War Mage. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |
| 워 메이지 | **War Mage** | Magic Johnson's combat-specialized Archmage title. |
| 총서기 | **General Secretary** | One of Xiao Yang's offices. |
| 국가 주석 | **state chairman** | Xiao Yang's office as leader of the People's Republic of China. |
| 중앙군사위원회 | **Central Military Commission** | Commission chaired by Xiao Yang. |
| 중국 공산당 | **Chinese Communist Party** | Party whose Central Military Commission Xiao Yang chairs. |
| 종석이 | **Jongseok** | Taekyung's mistaken personal-name joke for the General Secretary; not the chairman's actual name. |
| 파이 첸 | **Pai Chen** | S-rank Hunter, Great Cataclysm hero, and former romance-film actress. |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 윌리엄 | **William** | Prince Felix's formal attendant. |
| 필릭스 알렉산더 루이 | **Prince Felix Alexander Louis** | British prince and third in line to the throne. |
| 케임브리지 공작 | **Duke of Cambridge** | Title held by Prince Felix. |
| 스트래선 백작 | **Earl of Strathearn** | Title held by Prince Felix. |
| 캐릭퍼거스 남작 | **Baron Carrickfergus** | Title held by Prince Felix. |
| 가터 훈장의 기사 | **Knight of the Garter** | Honor held by Prince Felix. |
| 시슬 훈장의 기사 | **Knight of the Thistle** | Honor held by Prince Felix. |
| 아레스 길드 | **Ares Guild** | Powerful Guild whose practical leader is Lee Jungryong. |
| 랴오 상장 | **Senior General Liao** | Chinese Senior General and member of the Princelings faction. |
| 태자당 | **Princelings** | The Communist Party's largest faction; Liao belongs to it. |
| 상하이방 | **Shanghai clique** | Faction associated with Xiao Yang and Wei Penghu. |
| 천안문 광장 | **Tiananmen Square** | Place referenced in Taekyung's hypothetical beheading joke. |
| 북경 | **Beijing** | Possible destination for teleported nuclear warheads. |

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
| 샤오 쉔 | 진태경 | foreign_hunter_to_recognized_hero | Teacher Jin | formal-polite | Uses 진 선생님 after recognizing Taekyung as Sibeol-jwa. |
| 스켈레톤 워로드 | 진태경 | undead_subordinate_to_human_controller | vile human | hostile-but-familiar | Recurring address used while speaking to Taekyung during the battle. |
| 진태경 | 스켈레톤 워로드 | human_controller_to_undead_subordinate | Boney | casual-teasing | Taekyung uses Boney as a deliberately demeaning pet nickname. |
| 웨이펑후 | 진태경 | senior_military_official_to_foreign_hero | Teacher Jin | respectful-formal | Wei Penghu uses 진 선생 when introducing himself and inviting Taekyung to the operations headquarters. |
| 조종사 | 웨이펑후 | pilot_to_senior_military_official | Comrade Minister of Defense | deferential-formal | Pilot's formal greeting on Wei Penghu's arrival. |
| 웨이펑후 | 샤오 쉔 | senior_military_official_to_subordinate_hunter | Senior Colonel Shao Shen | respectful-but-familiar | Wei Penghu uses Shao Shen's rank and name when bidding him farewell. |
| 샤오 쉔 | 웨이펑후 | subordinate_hunter_to_senior_military_official | Comrade Minister of Defense | deferential-formal | Shao Shen promises to complete his mission and rejoin Wei Penghu. |
| 샤오 양 | 진태경 | head_of_state_to_foreign_hunter | Teacher Jin | respectful-formal | Xiao Yang uses 진 선생 when greeting and addressing Taekyung. |
| 샤오 양 | 웨이펑후 | head_of_state_to_old_friend_and_subordinate | Minister of Defense Wei Penghu | authoritative-but-familiar | Xiao Yang addresses Wei by office and name while discussing authority over the Central Military Commission. |
| 웨이펑후 | 샤오 양 | subordinate_to_head_of_state | Comrade Chairman | deferential-formal | Wei uses 주석 동지 when responding to Xiao Yang. |
| 진태경 | 파이 첸 | junior_to_older_senior | Ms. Chen / Chen | polite-but-familiar | Taekyung initially uses Ms. Pai Chen; she permits Chen or older sister, but he rejects the latter after learning her age. |
| 우헤이싱 | 진태경 | hostile_peer | peninsula bangzi | abusive-hostile | Wu Heixing repeatedly addresses Taekyung with an anti-Korean slur. |
| 진태경 | 우헤이싱 | hostile_peer | mainland chink | abusive-hostile | Taekyung answers Wu Heixing's slur with an explicit anti-mainland insult. |
| 윌리엄 | 필릭스 알렉산더 루이 | attendant_to_royal_prince | His Royal Highness Prince Felix | deferential-ceremonial | William recites Felix's complete royal titles when instructing the room to show respect. |
| 필릭스 알렉산더 루이 | 윌리엄 | royal_prince_to_attendant | William | commanding-familiar | Felix stops William's repeated title recital by name. |
| 매직 존슨 | 이정룡 | senior_s_rank_hunter_to_peer | Lee | casual-flirtatious | Greets Lee Jungryong familiarly and jokes about confessing his love. |
| 이정룡 | 매직 존슨 | peer_s_rank_hunter | Magic Johnson | casual-but-respectful | Responds to Magic Johnson's flirtatious greeting. |
| 파이 첸 | 이정룡 | peer_s_rank_hunter | Mr. Lee | playful-polite | Responds to Lee's romantic joke with teasing politeness. |
| 우헤이싱 | 이정룡 | junior_s_rank_hunter_to_top_s_rank_hunter | Mr. Lee | intimidated-deferential | Uses 이 선생님 and suppresses his usual hostility in Lee's presence. |
| 필릭스 알렉산더 루이 | 이정룡 | royal_prince_to_top_s_rank_hunter | Jungryong Lee | formal-polite | Addresses Lee through the translation device without the expected royal honorific. |
| 이정룡 | 필릭스 알렉산더 루이 | top_s_rank_hunter_to_royal_prince | that prince | casual-dismissive | Does not use the prince's formal title. |
| 웨이펑후 | 이정룡 | senior_military_official_to_top_s_rank_hunter | Mr. Lee | respectful-formal | Addresses Lee as 이 선생 during the meeting. |
| 랴오 상장 | 웨이펑후 | senior_general_to_minister_of_defense | Comrade Minister of Defense | blunt-but-formal | Challenges Wei Penghu's strategy while invoking factional rivalry. |
| 웨이펑후 | 랴오 상장 | minister_of_defense_to_senior_general | Senior General Liao | formal-authoritative | Invites Liao to speak and later rebukes his nuclear proposal. |

## Exact glossary matches

| 무림     | **Murim**          |
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 검법     | **sword technique**                              |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 장비               | **Equipment**                  |
| 습득               | **Acquired**                   |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 공자      | **Young Master**                                                |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |

## Listed compact profiles

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 386
- **Aliases:** None
- **Role:** S-rank Hunter and highly media-exposed Chinese Hunter
- **Personality:** Arrogant, volatile, status-conscious, and attention-seeking
- **Voice:** Aggressive, insulting, and indignant
- **Relationships:** Antagonizes Jin Taekyung and resents the attention Taekyung receives from Xiao Yang; rumored to be the son of a senior Communist Party official.

## Korean source

```text
＃387화



지하 벙커를 빠져나왔을 때는 이미 깊은 밤이었다.

크게 숨을 들이쉬자 차가운 공기가 폐부로 스며든다. 저 어딘가에 있을 무림의 사천을 떠올리며 별이 총총히 박힌 밤하늘을 바라보고 있는데, 자그마한 손이 어깨를 톡 건드렸다.

「따라올래? 가볍게 한잔할 생각인데.」

“지금요?”

「응. 우리끼리.」

파이 첸이다. 그녀의 등 뒤에는 ‘우리’에 속한 두 사람이 서 있었다.

그중 하나가 기품이 넘쳐흐르는 말투로 입을 열었다.

「동양의 귀부인이여, 혹 함께 마실 술 중에 로마네콩티가 있는가?」

「귀부인은 아닌데, 당연히 있지. 술 좋아해, 왕자?」

필릭스 왕자가 못마땅한 얼굴로 대답했다.

「왕자가 아니라 필릭스 전하라고 부르라니까. 그리고 술은 적당히 즐기는 편이다. 특히 로마네콩티 45년 산을.」

「45년 산은 없는데.」

「그럼 거절하지. 난 이만.」

저거 진짜 미친놈인가.

필릭스 왕자가 수행원들을 이끌고 사라지자 파이 첸이 남은 한 사람을 향해 고개를 돌렸다.

「당신은 갈 거지. 존슨?」

매직 존슨이 새하얀 이빨을 드러내며 웃었다.

「미안하군. 아쉽지만 다음으로 미뤄야 할 것 같아.」

「왜?」

「당장 내일 전선에 투입될지도 모르는데, 메모라이즈(Memorize) 정도는 해 둬야 마음이 편할 것 같아서.」

역시 대마법사. 대격변의 영웅은 괜히 되는 게 아니구나.

매직 존슨의 마음가짐에 깊은 감명을 받은 내가 입술을 뗐다.

“저도 지금은 안 될 것 같은데요.”

「안 돼.」

“왜요?”

「넌 왕자도 아니고, 대마법사도 아니잖아.」

“……아니, 그런 게 어딨어요.”

어이가 없네. 말도 안 되는 강짜를 놓는 건 둘째치고 이런 판국에 술을 마시자는 저 아줌마도 정말 어지간하다.

「너, 방금 속으로 내 욕했지? 이런 상황에서 술이나 마시는 생각 없는 아줌마라고.」

“……어떻게 알았어요?”

「어머, 얘 쓸데없이 솔직한 것 좀 봐라?」

파이 첸이 긴 손가락으로 내 코끝을 쿡 찔렀다. 외관만 보면 20대 초반의 미인인데, 실상은 어머니보다 나이 많은 사람이라 그런지 기분이 묘하다.

“다른 사람 찾아보시는 게 어때요? 이정룡 씨라거나…….”

「리(Lee)?」

파이 첸의 고개가 살짝 기울어졌다. 이정룡은 이미 자신이 데려온 아레스 길드원들과 사라진 지 오래였다.

「흠. 뭔가 어려운 사람이라서. 대격변 때만 해도 저 정도는 아니었는데 능구렁이가 다 됐어. 무슨 생각을 하는지 알 수가 없다니까.」

사람 보는 눈이 상당히 정확한데.

파이 첸은 저 멀리 사라지는 또 다른 후보를 힐끗 곁눈질하며 말을 이었다.

「우헤이싱. 쟤는 너무 예의가 없고. 같이 마시면 술맛 떨어져.」

나는 인적 드문 숲속으로 향하는 우헤이싱의 뒷모습을 물끄러미 바라보며 대답했다.

“어쩔 수 없네요. 다음에 드시는 수밖에.”

「아니. 술은 이런 날에 마시는 거란다.」

“……?”

「마지막이 될지도 모르잖니.」

“아.”

파이 첸이 왜 술을 찾는지, 어느 정도 알 것 같았다.

전쟁은 사람을 지치게 만든다. 동시에 죽음이라는 방식으로 예측하지 못한 이별이 찾아오기도 한다.

대격변을 통해 수많은 동료를 잃었던 그녀만의 전야제(前夜祭)인 셈이다.

당장 이번 사태가 마무리되었을 때, 우리 중 누군가는 영영 돌아올 수 없는 강을 건넜을 수도 있으니까.

「뭐, 어쨌건 이렇게 된 이상 표적을 바꾸는 수밖에 없네. 안 그래, 거기 잘생긴 총각?」

“저 안 간다니까요.”

파이 첸이 어처구니없는 표정으로 나를 바라봤다.

「양심이 없니? 너 말고 저 청년 말이야.」

파이 첸에게 지목당한 잘생긴 총각, 최 팀장은 내 예상과 다르게 흔쾌히 고개를 끄덕였다.

“불러 주신다면 저야 영광입니다.”

“어, 팀장님. 진짜 가시게요?”

“가야죠. 파이 첸과 함께 술자리를 가질 기회가 언제 또 오겠습니까. 궁금한 것도 많고요.”

파이 첸이 까르르 웃었다.

「잘생긴 줄만 알았는데 말도 예쁘게 하네. 그래, 뭐가 그렇게 궁금하니?」

“혹시 지금 착용하고 계신 장비. 어디서 구매하신 겁니까?”

「……그게 질문이야?」

“예.”

「얘도 만만치 않네.」

한숨을 푹 내쉬는 파이 첸을 보며 매직 존슨이 호탕한 웃음을 터트렸다.

「하하. 미스 첸, 그럼 이제 다 같이 한잔하러 갈까?」

「다 같이? 존슨 당신 안 간다고 하지 않았어?」

「그랬지. 여자랑 단둘이 술 마시는 취미는 없거든. 하지만 여기 있는 미스터 최처럼 매력적인 남자가 동석한다면 이야기는 달라지지.」

「…….」

「난 남자가 좋아. 특히 동양인 남자.」

「그, 그래. 가자.」

역시 타임지가 선정한 세상에서 가장 영향력 있는 성소수자 1위답다.

나는 바짝 굳은 채 끌려가는 최 팀장에게 전음을 날렸다.

- 무슨 일 생기면 연락해요.

도살장에 끌려가는 소처럼 슬픈 눈으로 나를 바라본 최 팀장이 두 S급 헌터와 함께 사라지고, 주위를 둘러본 나는 발걸음을 옮겼다.

‘이 방향이었지.’

사람들의 눈을 피해 어두컴컴한 오솔길을 얼마나 걸었을까. 컴컴한 어둠 속에 멈추어 서서 입을 열었다.

“나와.”

잠깐의 침묵 후, 누군가의 목소리가 흘러나왔다.

「……제법이군.」

부스럭.

인기척과 함께 나타난 한 사람, 우헤이싱이 나를 위아래로 훑었다.

「어떻게 알았지?」

저걸 말이라고. 나는 심드렁하게 대꾸했다.

“차라리 일 더 하기 일이 뭐냐고 물어봐라. 그게 더 어렵겠다.”

「음. 생각보다 실력 있는 놈이었군.」

“이제 와서 칭찬하는 척하지마. 개수작 부리려는 거 뻔히 보이니까.”

「……!」

정곡을 찔린 우헤이싱의 얼굴이 붉게 달아올랐다.

어떤 의미에서는 참 다루기 쉬운 놈이다. 서른 중반이 넘은 나이로 알고 있는데 저렇게 단순하기도 힘들다.

「그, 그게 아니라 나는 진심으로…….」

“진심으로 빵즈라고 생각하겠지. 아직 정식 S급 헌터도 아닌 웬 한국놈이 너 대신 주목받으니까 짜증 났을 거고. 특유의 일차원적인 행동으로 시비부터 걸고 봤는데, 이게 영 반응도 안 좋고 저 빵즈 놈도 생각 외로 만만치가 않네?”

나는 대꾸할 틈도 주지 않고 속사포처럼 말을 이었다.

“그래서 괜히 마음에도 없는 칭찬 몇 번 날려 주고, 우호적인 제스처 취하면서 뭔가 수작을 부리려는 것 같은데…… 아, 혹시 지금까지 내가 말한 것 중에 틀린 부분 있냐?”

「…….」

“그래, 너 같은 놈 많이 봤다. 뒤통수를 하도 처맞았더니 안 돌아가던 머리가 휙휙 돌아가더라.”

한심한 눈빛으로 바라보자, 얼굴이 벌겋게 달아올라 있던 우헤이싱이 더듬더듬 입을 열었다.

「다른 수작을 부리려던 건 아니었다.」

“아니면? 혹시 나랑 친해질 생각이면 곱게 접어서 넣어 둬라. 똥 옆에 있으면 나한테까지 냄새 배니까.”

「……!」

“그런데 너 지금 뭐 하냐?”

내 나직한 한마디에, 검파를 향해 움직이던 놈의 손이 우뚝 멈췄다.

“뽑지 마라. 다친다.”

갈등 어린 눈빛으로 날 바라보던 우헤이싱이 불쑥 입을 열었다.

「어차피 다 알고 있었으면서…… 왜 순순히 따라온 거지?」

“물어볼 게 있어서.”

「뭐?」

난 우헤이싱의 눈동자를 똑바로 직시하며 입을 열었다.

“전음(傳音). 맞지?”

「……!」

딱딱하게 굳은 얼굴이 곧 대답이다. 설마 했는데, 나는 뒷머리를 긁적이며 중얼거렸다.

“맞나 보네. 하긴, 본토니까 여러 가지 무공이 남아 있을 수도 있겠지. 내공심법이라던가.”

「무, 무슨 소리! 그건 메시지 마법…….」

“얼씨구.”

황급히 변명을 늘어놓는 녀석의 모습에 실소가 흘러나왔다.

무공을 접하지 못한 다른 사람들은 차이점을 구분할 수 없겠지만, 나까지 속일 수는 없다.



‘잠깐 나 좀 보지.’



회의가 끝날 무렵 귓가에 닿은 것은 분명 전음이었다.

무시할 수도 있었던 제의에 응했던 이유는, 전음을 보낸 장본인이 바로 우헤이싱이었기 때문이다.

「네, 네놈이 그걸 어떻게.」

“왜, 아무도 모르는 비밀이었어?”

나는 당황하는 우헤이싱을 물끄러미 바라보며 입을 열었다.

“어느 정도 가능성은 있다고 생각하긴 했는데, 확실히 신기하긴 하네. 너희 문화 대혁명이다, 뭐다 해서 무술인들 싹 다 조져 놓지 않았었냐? 그 와중에도 용케 무공이 남아 있었네.”

「주둥이 닥쳐!」

“아, 너 집안 빵빵하다고 했었지. 그럼 공산당 최고위층이 직위를 이용해서 슬쩍 빼돌린 건가?”

「…….」

순식간에 착 가라앉은 표정을 보니 맞는 것 같다.

엄연한 외국인인 나로서는 이게 얼마나 큰 문제인지는 잘 모르겠지만, 내공심법. 즉 현대에 이르러 마나 연공법이라 불리는 이것의 가치가 어느 정도인지 알고 있다.

‘이곳이 무림이었다면, 한바탕 피바람이 일었겠지.’

그렇게 몰래 빼돌린 금송아지를 들켰으니, 놈의 반응이 좋지 않은 것은 당연했다.

「방금 했던 말, 두 번 다시 발설하지 않는 것이 좋을 거다.」

“딱히 할 생각은 없었는데, 말투가 상당히 띠껍네.”

우헤이싱이 표독스러운 눈빛으로 나를 노려보았다.

「내 아버지가 누군지 안 후에도 네놈이 이런 식으로 나올 수 있을까?」

“네 아버지가 누군진 모르겠고, 홍위병 출신이었을 것 같긴 한데.”

「……!」

“소싯적에 오함마 들고 공자 묘 때려 부순 게 너희 아버지 아니냐?”

「이 빵즈 새끼가-!」

파팟!

분기탱천한 고함과 함께 놈의 신형이 쏘아졌다.

어느새 검집에서 뽑혀 나온 직검(直劍)에서 솟구친 오러 블레이드, 아니 검강이 내 목을 노리고 날아든다.

쉬이이이잉!

시원한 바람에 머리카락이 흩날렸다. 바닥에 닿을 만큼 허리를 젖혀 검강을 피해 낸 나는, 몸을 튕기듯 일어나며 무릎으로 놈의 턱을 쳐올렸다.

콰직!

허공으로 솟구치는 치아와 핏물. 순간 비틀거리는 놈의 두 팔을 움켜잡고 귓가에 속삭였다.

“그 검. 뽑지 말랬지.”

치이이익, 우두둑!

「크아아아악!」

양손에 실린 강대한 열양지기가 갑옷을 부수고 살을 태운다.

우헤이싱의 입술 사이로 뛰쳐나온 비명은 내가 펼쳐 놓은 기막(氣幕)에 가로막혀 나아가지 못했다.

「노옴!」

후우우웅!

이놈, 권각술(拳脚術)까지 익혔다. 허접한 검법과는 달리 이건 제법 예리하다.

물론…….

‘무림이랑 비교하면 무공의 질이 훨씬 떨어져.’

나는 약간의 실망을 느끼며 손을 뻗었다.

꽈앙!

공력과 공력의 격돌.

내 허리를 향해 채찍처럼 휘둘러진 놈의 다리는 더 이상 나아가지 못했다.

우헤이싱의 눈동자가 충격과 경악으로 파르르 떨렸다.

「어, 어떻게?」

“잘.”

발목을 덥석 붙잡은 나는 땅을 향해 있는 힘껏 놈을 패대기쳤다.

후우웅, 콰앙!

한 번 더.

후우우웅, 쾅!

더, 더, 더.

쾅! 쾅! 콰과광!

땅이 뒤집히고 바위와 나무가 뽑혀 나간다.

잠시 후 생체 곡괭이질이 멈췄을 때는, 혼이 빠져나간 듯한 우헤이싱이 커다란 크레이터 안에 대자로 뻗어 있었다.

“그래도 몸은 튼튼해서 별로 안 다쳤네.”

「흐, 흐어…….」

“야, 우냐?”

「흐어어어…….」

아주 정신이 나갔군.

혀를 차며 허리를 굽힌 나는 놈의 주머니를 뒤졌다.

공간 확장 마법이 걸린 주머니를 얼마나 헤집었을까, 마침내 원하던 물건을 찾을 수 있었다.

“아, 여기 있네. 상급 포션.”

띠링.



- [최상급 포션]을 습득하셨습니다!



“……이 아니라. 최상급 포션? 뭐야, 이 새끼.”

나는 놀란 눈으로 뻗어 있는 우헤이싱을 바라봤다. 아무리 S급 헌터라지만 이런 물건을 들고 다니다니.

상급 포션도 희귀하지만, 최상급 포션은 일 년에 한두 개 나올까 말까 하는 물건이다.

현실감조차 들지 않는 가격은 둘째치고, 희소성이 너무 높은 탓에 돈이 있어도 못 구한다.

‘인터넷에서나 보던 걸 여기서 보네.’

잠시 고민하던 나는 최상급 포션을 슬쩍 인벤토리에 집어넣었다. 그리고 놈의 주머니를 뒤져 상급 포션 하나를 찾아내 부어 주었다.

“합의금 챙겼으니까 이쯤에서 봐준다. 너도 켕기는 거 많으니까 오늘 일 어디 가서 떠들면…… 알지?”

「흐으, 흐으으으…….」

“오케이. 우리 합의 본 거야.”

깔끔하게 사태를 마무리한 그때, 주머니에 넣어 둔 휴대폰이 부르르 몸을 떨었다.

최 팀장으로부터 짤막한 문자 한 통이 와 있었다.



〈 최 팀장님



최 팀장님

지ㄴ태경시제발빠ㄹ리 와주세요



“…….”

안 돼, 존슨.
```

## Final English reading copy

```markdown
# Chapter 387

By the time we left the underground bunker, it was already deep into the night.

I drew in a deep breath, and the cold air seeped into my lungs. As I gazed up at the star-filled night sky, thinking of the Sichuan of the Murim somewhere out there, a small hand tapped me on the shoulder.

“Want to come along? I was thinking of having a light drink.”

“Now?”

“Yeah. Just us.”

It was Pai Chen. Two people who belonged to her “us” stood behind her.

One of them spoke in a voice overflowing with dignity.

“O noblewoman of the East, might there be a bottle of Romanée-Conti among the wine we shall drink together?”

“I’m not a noblewoman, but of course there is. Do you like wine, Prince?”

Prince Felix answered with an displeased expression.

“I told you to call me His Highness Felix, not Prince. And I enjoy wine in moderation. Especially forty-five-year-old Romanée-Conti.”

“We don’t have any forty-five-year-old.”

“Then I must decline. I’ll be going.”

*Is he actually insane?*

As Prince Felix disappeared with his attendants, Pai Chen turned toward the one person left.

“You’re coming, right, Johnson?”

Magic Johnson smiled, baring his perfectly white teeth.

“I’m sorry. Unfortunately, I think I’ll have to take a rain check.”

“Why?”

“I might be deployed to the front tomorrow. I should at least use *Memorize* so I can put my mind at ease.”

As expected of an Archmage. You didn’t become a hero of the Great Cataclysm for nothing.

Deeply impressed by Magic Johnson’s attitude, I opened my mouth.

“I don’t think I can go right now either.”

“No.”

“Why not?”

“You’re neither a prince nor an Archmage.”

“…”

“What kind of logic is that?”

Unbelievable. Setting aside the ridiculous stubbornness she was displaying, that middle-aged woman was really something for suggesting drinks in a situation like this.

“You just insulted me in your head, didn’t you? You called me a clueless middle-aged woman for thinking about drinking in a situation like this.”

“...How did you know?”

“Oh my, look how pointlessly honest you are.”

Pai Chen poked the tip of my nose with one long finger. She looked like a beautiful woman in her early twenties, but in reality, she was older than my mother. It gave me a strange feeling.

“How about finding someone else? Mr. Lee, maybe…”

“Lee?”

Pai Chen tilted her head slightly. Lee Jungryong had disappeared a long time ago with the Ares Guild members he had brought along.

“Hmm. He’s a difficult man. He wasn’t like that during the Great Cataclysm, but he’s become a slippery old fox. You can’t tell what he’s thinking.”

*She’s a pretty accurate judge of character.*

Pai Chen continued, casting a sidelong glance at another candidate disappearing in the distance.

“Wu Heixing. He’s too rude. Drinking with him would ruin the taste.”

I stared at Wu Heixing’s back as he headed toward a deserted forest and answered.

“Nothing we can do. You’ll have to drink next time.”

“No. This is exactly when you’re supposed to drink.”

“...?”

“It might be the last chance we get.”

“Ah.”

I thought I understood, at least to some extent, why Pai Chen wanted a drink.

War exhausted people. At the same time, it brought unexpected farewells in the form of death.

It was her own sort of prewar celebration after losing countless companions during the Great Cataclysm.

Once this crisis was over, one of us might have crossed the river from which no one returned.

“Well, now that things have turned out this way, I have no choice but to change targets. Don’t you agree, handsome bachelor over there?”

“I told you I’m not going.”

Pai Chen stared at me in disbelief.

“Do you have no conscience? I’m talking about that young man, not you.”

The handsome bachelor Pai Chen had singled out, Team Leader Choi, nodded readily—contrary to my expectations.

“If you’ll have me, I’d be honored.”

“Wait, Team Leader. You’re really going?”

“I should. When will I get another chance to have a drink with Pai Chen? And I have a lot of questions.”

Pai Chen burst into laughter.

“I thought you were only handsome, but you say such pretty things, too. All right, then. What are you so curious about?”

“For the Equipment you’re wearing right now. Where did you buy it?”

“...That’s your question?”

“Yes.”

“This one’s quite a handful too.”

As Pai Chen let out a deep sigh, Magic Johnson broke into a hearty laugh.

“Haha. Miss Chen, shall we all go have a drink now?”

“All of us? Johnson, didn’t you say you weren’t coming?”

“I did. I don’t make a habit of drinking alone with women. But if a charming man like Mr. Choi joins us, that changes things.”

“…”

“I like men. Especially East Asian men.”

“Y-yes. Let’s go.”

No wonder Time had named him the world’s most influential LGBTQ person.

I sent Sound Transmission to Team Leader Choi as he was dragged away, stiff as a board.

—If anything happens, contact me.

Team Leader Choi looked at me with the sad eyes of an ox being led to slaughter, then disappeared with the two S-rank Hunters. I looked around before setting off.

*This was the direction.*

How long had I walked along the dark path to avoid people’s eyes? I stopped in the pitch-black darkness and spoke.

“Come out.”

After a brief silence, someone’s voice drifted out.

“...Not bad.”

Rustle.

A figure emerged with the sound of someone approaching. Wu Heixing looked me up and down.

“How did you know?”

*What kind of question was that?*

I answered listlessly.

“You might as well ask me what one plus one is. That’d be harder.”

“Hmm. You’re more capable than I expected.”

“Don’t pretend to compliment me now. It’s obvious you’re trying to pull some kind of cheap trick.”

“...!”

I had hit the mark. Wu Heixing’s face flushed red.

In a way, he was incredibly easy to handle. I believed he was already in his mid-thirties, yet it was hard to imagine anyone being this simple.

“N-no, that’s not it. I sincerely—”

“You probably do sincerely think I’m a *bangzi*.[^1] You were annoyed because some Korean guy who isn’t even an official S-rank Hunter yet was getting attention instead of you. You picked a fight with your usual one-dimensional behavior, but it didn’t go over well, and that *bangzi* bastard turned out to be tougher than you expected, huh?”

I continued speaking like a machine gun without giving him a chance to respond.

“So you threw out a few compliments you didn’t mean and started acting friendly while looking for an angle… Am I wrong about anything I’ve said so far?”

“…”

“Yeah, I’ve seen plenty of people like you. After getting hit in the back of the head so many times, even my brain—which had stopped working—started spinning again.”

I looked at him with pity. His face already bright red, Wu Heixing stammered.

“I wasn’t trying to pull any other kind of trick.”

“Then what? If you’re thinking of becoming friends with me, fold that thought up neatly and tuck it away. If I stand next to shit, the stink rubs off on me too.”

“...!”

“By the way, what are you doing right now?”

At my quiet question, the hand moving toward his sword hilt stopped dead.

“Don’t draw it. You’ll get hurt.”

Wu Heixing looked at me with hesitation in his eyes before blurting out,

“You knew all along… so why did you follow me so readily?”

“Because I had something to ask.”

“What?”

I looked directly into Wu Heixing’s eyes and spoke.

“Sound Transmission. Right?”

“...!”

His face stiffened. That was answer enough. I had suspected as much, but I scratched the back of my head and muttered,

“So it was. Well, this is the mainland, after all. There could still be all kinds of martial arts here. An internal-energy cultivation technique, for example.”

“W-what are you talking about? That was Message Spell…”

“Oh, please.”

A quiet laugh escaped me at his frantic excuses.

People who had never encountered martial arts might not be able to tell the difference, but he couldn’t fool me.

*Come see me for a moment.*

The thing that had reached my ear near the end of the meeting had unmistakably been Sound Transmission.

The reason I had accepted an offer I could have ignored was because Wu Heixing himself had been the one to send it.

“H-how did you know that?”

“What, was it a secret no one else knew?”

I stared at the flustered Wu Heixing and continued.

“I did think it was somewhat possible, but it’s still fascinating. Didn’t you wipe out all the martial artists during your Cultural Revolution and whatnot? Martial arts somehow survived even through that.”

“Shut your mouth!”

“Ah, you said your family was powerful. Did the highest levels of the Communist Party use their positions to quietly spirit it away?”

“…”

His expression instantly sank.

*Looks like I was right.*

As a foreigner, I didn’t know exactly how serious a problem this was. But I knew how valuable an internal-energy cultivation technique was—the thing now called a mana cultivation method in the modern era.

*If this were the Murim, a bloody storm would have erupted.*

Now that he’d been caught with the golden calf that had been secretly spirited away, it was only natural that he’d react badly.

“It would be best if you never uttered what you just said again.”

“I wasn’t planning to, but your tone is pretty damn irritating.”

Wu Heixing glared at me viciously.

“Even after you find out who my father is, do you think you can keep acting like this?”

“I don’t know who your father is, but I have a feeling he used to be a Red Guard.”

“...!”

“Wasn’t your father the one who smashed Confucius’s tomb with a sledgehammer in his youth?”

“You fucking bangzi bastard—!”

Fwish!

With an enraged roar, his body shot forward.

A straight sword had already been drawn from its scabbard. The Aura Blade rising from it—no, the Sword Force—flew toward my neck.

Shiiiiing!

The rush of wind scattered my hair. I bent backward until my back nearly touched the ground, avoiding the Sword Force, then sprang upright and drove my knee into his chin.

Crack!

Teeth and blood shot into the air. As he staggered, I seized both his arms and whispered into his ear.

“I told you not to draw that sword.”

Hiss, crack!

“Gaaaaaaaaah!”

The powerful Scorching Yang Qi surging through both my hands shattered his armor and seared his flesh.

His scream could not travel beyond the Qi Curtain I had spread.

“You bastard!”

Whooom!

That bastard had learned fist-and-foot techniques too. Unlike his shoddy sword technique, this one had some bite.

Of course…

*Compared with the Murim, the quality of his martial arts was far lower.*

Slightly disappointed, I reached out.

Boom!

Internal energy collided with internal energy.

The leg he had whipped toward my waist like a lash could go no farther.

Wu Heixing’s eyes trembled with shock and disbelief.

“H-how?”

“Well.”

I grabbed his ankle and slammed him into the ground with all my strength.

Whoom! Boom!

Once more.

Whoooom! Crash!

More. More, more, more.

Crash! Crash! KRA-KOOM!

The ground turned over, and rocks and trees were ripped from the earth.

A little while later, when I finally stopped using him as a living pickaxe, Wu Heixing lay spread-eagled in a huge crater, looking as if his soul had left his body.

“Still, you’ve got a sturdy body. You’re not hurt that badly.”

“Hh… hhaa…”

“Hey, are you crying?”

“Hhaa…”

He was completely out of it.

Clicking my tongue, I bent over and searched through his pockets.

After rummaging through the pouch with spatial expansion magic for a while, I finally found what I wanted.

“Ah, here it is. An Advanced Potion.”

Ding.

> **System**
> **Acquired:** Supreme Potion!

“...No, wait. Supreme Potion? What the hell, you bastard?”

I stared at the sprawled-out Wu Heixing in shock. Even if he was an S-rank Hunter, who carried something like this around?

Advanced Potions were rare, but Supreme Potions were items of which only one or two appeared in an entire year, if that.

Putting aside the price, which didn’t even feel real, they were so scarce that they couldn’t be obtained even with money.

*I’d only ever seen one online. And now here it is.*

After a moment of thought, I quietly slipped the Supreme Potion into my inventory. Then I searched through his pouch again, found an Advanced Potion, and poured it over him.

“I’ve taken my settlement payment, so I’ll let you off here. You’ve got plenty to hide, so if you go blabbing about what happened today… you know what happens, right?”

“Hh… hhh…”

“Okay. We’ve reached a settlement.”

Just as I had neatly wrapped things up, the phone in my pocket began to vibrate.

I had received one short text message from Team Leader Choi.

> 〈 Team Leader Choi
>
> Team Leader Choi
>
> Ji[n] Taekyung, please come qui[c]kly.

“…”

*No, Johnson.*

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.
```
