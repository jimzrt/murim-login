<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0388.txt",
      "sha256": "42101357608853dbee08db91bbea4eaef6f2203d32d447a350ac565693e47e69",
      "bytes": 16073
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b6a68e2ff7dc5f16876be1358e169bb66636d65d47d06688ea030ab7557a82ab",
      "bytes": 5198
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f4353b294e65128ec1033ee5ed79bd9fac9641f5dd2b18f446b0c29d3aa9320d",
      "bytes": 12980
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b5ce224614dbb8a8b47f6989dca3e99c969f596601ae3abb36eb249f95bcf852",
      "bytes": 23802
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "57757727bed6f5b0f9e824443ed79b404eff78afb087b2c49a3b0df86a6446d6",
      "bytes": 458
    },
    {
      "path": "characters/Wei Penghu.md",
      "sha256": "2468de93cf4481c21ad855bf391b9154e8f5a80b558bb0c8106faccd834f3de1",
      "bytes": 607
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "b54c9cc4633bf1378246204bfc47354fb7770ca8fe2f9c6a342cff10a909d04f",
      "bytes": 509
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6c9ff9ab197b09739321da27c2dcf84484353cdea866091d902db8087fea70a1",
      "bytes": 9734
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 17190
}
-->

# Durable State Update — Chapter 388

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 388. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 388. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 388,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 388,
    "continuity_sources": [388],
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
    "Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission, raised his missing nephew Lei Fei as his own son, and Lei Fei remains missing with his Sichuan Hunters.",
    "Xiao Yang is Chairman of the Central Military Commission of the Chinese Communist Party, General Secretary, and state chairman of the People's Republic of China; he retains full authority over the crisis response.",
    "Team Leader Choi accompanies Taekyung and trusts him during the Chinese crisis; he has now sent Taekyung an urgent message asking him to return.",
    "The six S-rank Hunters at the temporary headquarters are assigned to six fronts, each supported by three Army and Air Force divisions and Public Security Armed Forces Hunters.",
    "Magic Johnson is an S-rank Hunter, one of three Archmages worldwide, and a combat-specialized War Mage.",
    "Pai Chen is an S-rank Hunter, Great Cataclysm hero, and former romance-film actress who appears much younger than her actual age.",
    "Wu Heixing is an S-rank Hunter known for heavy media exposure, anti-Korean hostility, and drug and sexual-assault scandals; he is rumored to be the son of a senior Communist Party official.",
    "Prince Felix Alexander Louis is a British prince, third in line to the throne, and holds multiple senior British titles; William serves as his formal attendant.",
    "The Sichuan Tang Clan was devastated by Dark Heaven, owes Taekyung's group a debt, and is considering relocation.",
    "The Chengdu International Airport attack involved an undead army controlled by three incomplete Arch Liches, all of whom Taekyung destroyed.",
    "The Skeleton Warlord absorbed the death energy of the remaining two Arch Liches and became much stronger, but the persistence and full extent of that increase remain unknown.",
    "Dark Heaven's agents, purpose, and connection to the hidden transport formation remain unresolved.",
    "Ae-hyang appears to serve an unidentified superior after a sinister red light entered her eyes, and the Sichuan Governor's false memorial remains unresolved.",
    "Lee Jungryong is the practical leader of Ares Guild and one of the world's top three S-rank Hunters; he recognizes Choi Minwoo's growth and that Jin Taekyung has crossed the wall.",
    "Wu Heixing used Sound Transmission and possesses martial-arts knowledge; Taekyung defeated him after he attacked, taking his Supreme Potion and leaving him with an Advanced Potion."
  ],
  "continuity_sources": [
    387
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "Lee Jungryong's purpose beyond attending the bunker meeting, Wu Heixing's reason for sending the Sound Transmission, and the cause of Team Leader Choi's urgent message remain unresolved."
  ],
  "safe_through": 387,
  "temporary_decisions": [
    "Use the current Korean source as authoritative; the skipped range is not accepted English continuity.",
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생 and Comrade Chairman for 주석 동지.",
    "Render 반도의 빵즈 as peninsula bangzi and retain the derogatory-slur footnote.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's jokes.",
    "Render established names and titles consistently, including Pai Chen, Wu Heixing, Prince Felix Alexander Louis, William, Senior General Liao, the Princelings, and the Shanghai clique; use Sound Transmission, Sword Force, Advanced Potion, and Supreme Potion here."
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
| 파이 첸 | 매직 존슨 | peer_s_rank_hunter_to_peer_s_rank_hunter | Johnson | casual-but-familiar | Uses his surname while inviting him to drink. |
| 매직 존슨 | 파이 첸 | peer_s_rank_hunter_to_peer_s_rank_hunter | Miss Chen | casual-polite | Uses a polite English honorific while inviting her to join the group. |
| 파이 첸 | 최 팀장 | senior_s_rank_hunter_to_trusted_ally | handsome bachelor | playful-familiar | Playful address while recruiting Team Leader Choi for the drinking party. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 레이페이 | **Lei Fei** | Previously undisclosed Chinese S-rank Hunter and commander of the Sichuan Public Security Armed Forces; missing with his Hunters. |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 열화신공 | **Blazing Flame Divine Art** | Art whose formula Taekyung uses to infuse the armor. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 386
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist who has crossed the wall; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 383
- **Aliases:** None
- **Role:** S-rank Hunter and commander of the Public Security Armed Forces stationed in Sichuan Province
- **Personality:** Not established in Chapter 383
- **Voice:** Not heard in Chapter 383
- **Relationships:** Wei Penghu's only nephew; his mother died in childbirth, and Wei Penghu raised him as his own son

### Wei Penghu.md

# Wei Penghu (웨이펑후)

- **Safe through:** Chapter 386
- **Aliases:** None
- **Role:** Senior General and Minister of Defense at the Central Military Commission
- **Personality:** Courteous, composed, and direct in his first meeting with Jin Taekyung
- **Voice:** Formal and respectful
- **Relationships:** Meets Jin Taekyung after the Chengdu International Airport battle, brings him toward the temporary operations headquarters, and is Lei Fei's uncle; he raised Lei Fei as his own son and asks Taekyung to bring him back if found.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 387
- **Aliases:** None
- **Role:** S-rank Hunter and highly media-exposed Chinese Hunter
- **Personality:** Arrogant, volatile, status-conscious, and attention-seeking
- **Voice:** Aggressive, insulting, and indignant
- **Relationships:** Antagonizes Jin Taekyung and resents the attention Taekyung receives from Xiao Yang; rumored to be the son of a senior Communist Party official.

## Korean source

```text
＃388화



“야, 야.”

툭, 툭툭.

옆구리를 건드리는 누군가의 발끝. 간신히 눈을 뜬 우헤이싱의 시야에, 자신을 내려다보는 커다란 형체가 어른거렸다.

「흐으…….」

“나 급한 일이 생겨서 이만 가 봐야 하거든? 혹시 누구 오거나 그러면 알아서 잘 둘러대라.”

「흐으, 흐으으…….」

“포션 부어 줬으니까 엄살 그만 피우고, 인마. 계속 그러면 매직 존슨 불러서 진짜 신음 흘리게 하는 수가 있어. 그럼 간다!”

파팟!

듣는 것만으로도 엉덩이가 욱신거리는 한마디를 남긴 채, 순식간에 멀어져 가는 한 사람의 인기척.

대 자로 뻗어 있던 우헤이싱이 끓어오르는 음성을 내뱉은 것은 그로부터 십여 분이 흐른 뒤였다.

「진태경……!」

부러진 뼈와 살은 상급 포션의 효능으로 회복되었지만, 뼛속 깊이 각인된 고통과 금이 간 자존심까지 치유할 수는 없었다.

‘도대체 어떻게?’

믿을 수 없었다. 제아무리 흥분한 상태였다고는 해도 S급 헌터인 자신이 이렇게까지 철저하게 농락당하다니.

진태경에게 무공을 간파당했다는 것도 충격이지만, 스스로가 지니고 있는 힘에 대단한 자부심을 가진 그로서는 패배에 대한 충격이 더 컸다.

‘내가, 다른 사람도 아닌 이 내가?’

우헤이싱은 태어남과 동시에 헌터의 운명을 타고났다.

그는 유아기 시절 막대한 금액을 들인 마나 적응도 검사를 통해 잠재력을 인정받았고, 중국 공산당 최고위층인 집안은 온갖 지원을 아끼지 않았다.

부패로 축적한 막대한 재산과 권력. 최고의 환경과 지원 아래 성장한 우헤이싱은 스무 살이 되던 해에 A급 헌터로 각성했고, 십 년이 흐른 뒤에는 S급 헌터가 되는 기염을 토했다.

그런데…….

‘그런데 어째서. 내가 저런 소국의 빵즈 놈에게!’

캄캄한 밤하늘을 노려보는 우헤이싱의 눈동자에 기광이 번뜩였다.

그의 눈빛에 서린 것은 분노인 동시에 질투였으며 진태경이 보여 준 힘에 대한 일말의 두려움이었다.

그리고 이러한 감정들은 우헤이싱이 지난 십수 년 동안 지긋지긋하게 느껴 온 것이기도 했다.

이제는 찾을 수 없는 한 사람을 향해, 우헤이싱이 외쳤다.

「네놈의 짓이냐? 죽어서도 날 괴롭히려는 거냐!」

대중과 미디어는 그를 구제 불능 탕아라 욕하는 동시에 중화가 낳은 천재라며 칭송했지만, 우헤이싱을 포함한 극소수의 사람들은 알고 있었다.

진정한 천재는 따로 있음을. 그렇기에 드러내지 않고 감춰 놓았다는 것을.

「대답해라, 레이페이!」

막강한 실력은 물론이고 고결한 심성을 지닌 레이페이는 우헤이싱에게 있어 넘을 수 없는 벽이었다.

처음 그가 실종되었다는 소식을 듣고 얼마나 당황하고 기뻐했던가.

하지만 불과 일주일 만에 또 다른 벽이 나타났다. 진태경이라는 이름으로.

「으아아아아!」

쩌렁쩌렁한 외침에 수풀이 몸을 부르르 떨던 그때였다.

“그 마음, 나도 잘 알지.”

기척도 없이 다가온 누군가의 나직한 목소리에, 우헤이싱은 번개처럼 몸을 일으켜 세웠다.

「누구냐!」

“섭섭하군. 구면이라고 생각했는데.”

저벅.

어둠 속에서 불쑥 걸음을 내디딘 한 사람. 우헤이싱의 눈동자가 크게 뜨였다.

「당신은……?」

희미하게 비치는 달빛 아래, 이정룡이 미소 띤 얼굴로 말을 이었다.

“우리가 긴히 나눌 이야기가 있을 것 같은데. 어찌 생각하나?”

「……!」



* * *



띠링.



- [운기조식]을 완료했습니다!

- [열화신공]의 경지가 미약하게 상승합니다!



기운을 갈무리하고 눈을 떴을 때는 밖이 환하게 밝아 오고 있었다.

마치 이때만을 기다리고 있었다는 듯 스켈레톤 워로드가 냉큼 입을 연다.

- 간악한 인간. 드디어 일어났나?

“안 잤어, 인마.”

- 전투를 앞두고 술을 마시다니. 쯧쯧.

“어차피 술병 날 일 없으니까 조용히 해라.”

술을 많이 마시면 주독(酒毒)이 쌓이는데, 어지간한 내가 고수라면 손쉽게 주독을 몰아낼 수 있다.

강대한 열양지기를 지닌 나는 말할 것도 없지.

‘그러고 보니 엄청나게 마시긴 했지. 파이 첸이 전용기로 실어 온 술을 몽땅 거덜 냈을 정도니까.’

분명히 매직 존슨을 말리러 간 거였는데, 어쩌다가 그렇게 됐는지 나도 잘 모르겠다.

- 그런데 인간. 언제까지 이런 갑갑한 곳에 있을 생각인가?

“안 그래도 갈 생각이야.”

시계를 보니 오전 다섯 시 반. 슬슬 준비해야 할 때다.

임시 숙소로 배정받은 호텔 룸에서 짐을 챙긴 뒤 로비로 내려가자, 커피를 마시고 있는 최 팀장이 보였다.

“어, 팀장님.”

“……나오셨군요.”

슬쩍 보니 눈 밑이 퀭하다. 평소 철저한 자기 관리로 잡티 하나 없던 피부가 까슬까슬해 보인다.

“혹시 안 주무셨어요?”

“진태경 씨 같으면 잠이 오겠습니까?”

“…….”

그건 그래.

어젯밤, 세상에서 가장 다급한 호출 문자를 받고 달려간 내가 목격한 광경은 참혹하기 그지없었다.



‘헤이, 최. 이건 술 게임이잖아. 쿨하게 한 번 하자고. 안 그래?’

‘파이 첸! 도와주십시오, 파이 첸!’

‘으음……. 미안한데 이건 술 게임인걸. 왕의 명령은 절대적이다. 이게 룰 아냐?’

‘아무리 그래도 뽀뽀라니! 저는 술 게임 자체도 처음이란 말입니다! 룰도 제대로 설명 안 해 주셨잖아요!’

‘아. 몰라, 몰라. 2번은 3번의 볼에 입 맞출 것. 이게 내 명령이야.’

‘최. 가만히 있어. 난 네게 속박 마법을 걸고 싶지 않아.’

‘이건 말도 안…… 진태경 씨! 여깁니다, 진태경 씨!’

‘진. 방해하지마. 난 네게 공격 마법을 쓰고 싶지 않아.’



정말이지, 일 분만 늦었어도 대참사가 벌어질 뻔했다.

최 팀장을 구제해 주는 대가로 엄청난 양의 술을 원샷 해야 했지만, 일말의 후회도 없다. 그에 걸맞은 합당한 보상을 약속받았으니.

“혹시 어제 했던 약속, 기억하시죠? 제 정산 비율 조정하기로 한 거.”

“……알고 있습니다. 9대1.”

최 팀장이 싸늘한 눈빛으로 나를 노려보았다.

“어떻게 그런 급한 상황에서 그러실 수가 있습니까? 사람입니까?”

“그럼 지금이라도 찐하게 뽀뽀 한번 하시든가. 마침 저기 오시네, 2번님.”

번호는 2번이지만 게이력은 세계 제일이지.

지금 막 로비에 들어선 거구의 흑인, 매직 존슨을 발견한 최 팀장이 마시고 있던 커피를 뿜었다.

“푸웁! 저 좀, 저 좀 숨겨 주십시오.”

“이미 늦은 것 같은데.”

내 말이 끝나기가 무섭게, 우리를 발견한 매직 존슨이 솥뚜껑만 한 손바닥을 흔들었다.

“헤이, 게이즈!”

보통은 가이즈 아닌가. 잘못 말한 거겠지……?

순간 귀를 의심하는 나와 최 팀장에게 다가온 매직 존슨이 껄껄 웃었다.

「너무 그런 표정 짓지 마. 어제는 내가 너무 흥분해서 아주 약간 장난친 거니까.」

“……진짜 흥분하셨어요?”

「아, 그게 그렇게 되네.」

“말조심해 주세요. 깜짝 놀랐네.”

「하하. 어쨌든 어제는 좀 사정이 있었어.」

“……뭐가 있었다고요?”

「어? 아니, 사정이 그 사정이 아니라.」

“말조심 좀 해 주세요. 진짜 깜짝 놀랐네.”

“제발 두 분 다 그만하시죠. 누가 들을까 봐 겁납니다.”

해탈한 얼굴로 남아 있던 커피를 원샷한 최 팀장이 고개를 돌렸다.

어느새 호텔 정문을 통과한 한 무리의 사람들이 우리를 향해 걸어오고 있었다.

「이제 떠날 시간이오. 선생들.」

그중 선두에 있던 국방부장 웨이펑후의 목소리는 긴장으로 딱딱하게 굳어 있었다.

그의 눈짓에 나이 지긋해 보이는 군 장성 하나가 서류철을 하나씩 나눠 주었다.

“이게 뭡니까?”

「선생들이 배치된 지역과 주둔 병력에 대한 정보요. 물론 저쪽에도 미리 필요한 정보와 연락은 취해 두었소. 지금부터는 지정된 제트기를 타고 이동할 거요.」

아무래도 최첨단 기술이 발달한 현대이다 보니, 이런 것만큼은 편리하다.

잠시 후 웨이펑후의 뒤를 따라 도착한 임시 이륙장에는 삼엄한 경호에 둘러싸인 익숙한 얼굴들이 있었다.

「잘 잤니, 젊은이들?」

「…….」

“늦었군.”

기지개를 쭉 켜며 인사를 건네는 파이 첸. 어제 있었던 일 때문인지 말없이 시선을 내리까는 우헤이싱과 묘한 미소를 짓고 있는 이정룡까지.

인벤토리 안에 고이 넣어 둔 스켈레톤 워로드가 떨떠름한 목소리로 말했다.

- 왠지 모르게 기분 나쁜 인간이로군. 본 사령관은 저자가 썩 마음에 들지 않는다.

“동감이야.”

작게 중얼거린 소리를 들은 파이 첸이 눈썹을 치켜올렸다.

「응? 뭐라고?」

“아닙니다. 그나저나 필릭스 왕자는요?”

「동트기 직전에 떠났어. 왕자가 맡게 된 지역에서 교전 신호가 왔다던데.」

“……그렇군요.”

도착한 지 24시간도 되지 않아 또다시 전투가 벌어지다니.

새삼 전쟁이라는 두 글자에 문득 가슴 한구석이 꾸욱, 하고 조여 온다.

국적도, 자라난 환경도 다르지만 나와 같은 인간이 어딘가에서 무참히 살육당하고 있다고 생각하니 마음이 무거워졌다.

「거기 젊은이.」

“예?”

나를 물끄러미 바라보던 파이 첸이 어깨를 툭 쳤다.

「어깨에 힘 풀어. 무거워서 창이나 제대로 휘두르겠어?」

“…….”

「자책하지도 말고 조급해할 필요도 없어. 모든 죽음에 책임을 지려 하지 말라고.」

책임이라. 잠깐 고민하던 나는 솔직히 대답했다.

“……글쎄요. 그다지 자신은 없네요.”

「뭐, 그런 것치고는 어제 술을 진탕 퍼마시긴 하던데.」

“그건…….”

「알아, 농담이야. 우리 같은 사람들은 그렇게라도 잠시 부담감을 잊는 거지. 당장 내일, 아니 오늘 죽을지도 모르는 목숨이니까.」

밝은 목소리에 어울리지 않는 내용. 대격변이라는 소용돌이를 온몸으로 헤쳐나온 영웅은 고개를 들어 하늘을 바라보았다.

「아, 싸우기 딱 좋은 날씨다.」

그러고는 몸을 돌려 이륙 준비를 끝마친 제트기를 향해 사뿐사뿐 걸음을 옮긴다.

나직한 한마디를 남긴 채.

「모두…… 살아서 보자.」

그녀의 뒷모습이 기체 내부 안으로 사라졌다.

잠시 감회에 찬 눈빛으로 하늘을 올려다보던 매직 존슨이 불쑥 입을 열었다.

「헤이, 최.」

“네?”

「너도 엉덩이에 힘 풀어.」

“…….”

「아니, 어깨에 힘 풀어. 살아서 다시 보자고.」

저거 아무래도 진심이 나온 것 같은데.

최 팀장의 경계 어린 눈빛에 껄껄 웃은 매직 존슨이 파이 첸의 뒤를 이어 기체에 몸을 실었다.

이어 우헤이싱이 도망치듯 발걸음을 옮겼고, 마지막으로 남은 이정룡이 묘한 눈빛으로 나와 최 팀장을 훝었다.

“둘 다 몸조심하게. 이런 곳에서 요절할 수야 없지 않나. 젊은 나이에.”

노인네 말본새 하고는. 정말이지, 의미심장한 한마디다.

얼굴을 굳힌 최 팀장을 대신해, 내가 웃으며 입을 열었다.

“그래야죠. 우린 누구와 다르게 지금 죽어도 호상(好喪)은 아니니까.”

“……!”

“혹시 골로 가시면 부조 넉넉하게 하겠습니다.”

“기대하지.”

짧은 침묵 끝에 한마디를 툭 내뱉은 이정룡이 아레스 길드원들을 이끌고 멀어져 간다. 이제 남은 것은 우리뿐.

있는 힘껏 기지개를 켠 나는 최 팀장의 어깨를 두드렸다.

“가시죠. 팀장님.”

“예. 그래야죠.”

“긴장할 것 없습니다. 엉덩이에 힘 푸세요.”

“…….”

“……농담이었는데. 죄송합니다.”

농담 두 번 하면 사람 죽일 기세다.

슬금슬금 최 팀장의 눈치를 살피며 기체에 오르던 그때였다.

「부대- 차렷!」

등 뒤에서 터져 나온 우렁찬 외침.

국방부장 웨이펑후가 반백의 머리를 흩날리며 우리를 향해 거수경례를 올리고 있었다.

그러자 이륙장을 가득 메운 사람들이 웨이펑후를 따라 경례 자세를 취했다.

자신들의 가족과 친구들을 위해 싸우러 가는 영웅들을 향한 경의.

그들의 경례는 제트기의 문이 닫히고, 까마득한 점이 되어 시야에서 사라질 때까지 끝나지 않았다.

‘거, 참.’

이렇게까지 해 주니 어깨가 무거워질 수밖에.

문득 피로를 느끼며 시트에 몸을 기댄 다음 순간이었다.

치직. 치지직.

- ……답. 응답하라. 여기는…….

갑자기 조종석에서 들려오는 노이즈 낀 무전과 함께 귓속을 파고드는 알림.

띠링.



- 돌발 퀘스트, [다급해진 전황]이 생성되었습니다.

- 당신은 퀘스트를 거절할 수 없습니다. 한시라도 빠르게 도착하여 적들을 물리치십시오!



“…….”

빌어먹을, 내 인생이 이렇지 뭐.

푹 한숨을 내쉰 나는 조종석을 향해 힘차게 외쳤다.

“아저씨, 풀 악셀 땡겨요!”



* * *



「그들은?」

입을 연 것은 팔십 대의 노인이었다. 주름과 검버섯이 가득한 얼굴. 늙은 육신은 소싯적만 못했지만, 그의 눈동자에는 젊었을 적보다 더한 힘이 있었다.

홀로그램 화면으로도 느껴지는 노인의 힘 있는 눈빛에, 마른침을 삼킨 웨이펑후가 대답했다.

「모두 출발했습니다. 주석 동지.」

「전황은 어떤가?」

「마법으로 인한 통신 교란과 결계로 적들의 동태를 쉽게 파악할 수 없습니다만, 최선을 다해 이동을 감지 중입니다.」

「S급 헌터들이 도착한다면…….」

「그들의 힘이라면 충분히 전황을 뒤집을 수 있습니다.」

「속단은 금물이야. 한순간도 방심하지 말게. 수많은 이들의 목숨이 우리의 결정에 달렸네.」

「예. 명심하겠습니다.」

웨이펑후 국방부장과의 짧은 통신이 끝난 후, 샤오 양 중국 주석은 드넓은 회의실에 앉아 생각에 잠겼다.

‘어쩌다 이리되었는지.’

대격변 이후 유례없는 대참사다. 수많은 인력과 자금을 투입했지만 아크 리치를 중심으로 한 몬스터 군단을 막을 수는 없었다.

가급적이면 혼란을 막고 싶었지만…… 더 이상 늦으면 기회는 영영 사라질지도 모른다.

그렇기에 샤오 양은 공산당 내부의 숱한 반대를 무릅쓰고 오늘, 이 자리에 왔다.

「준비되었습니다.」

「……즉시 연결하게.」

비서관의 말에 샤오 양은 감았던 눈을 떴다.

넓은 회의실, 비어 있던 자리 위로 홀로그램으로 이루어진 형체들이 하나둘씩 떠오르기 시작했다.

인종도, 성별도 모두 다른 열넷. 아니 샤오 양을 포함한 열다섯 명의 사람들.

그들 한 사람, 한 사람은 일국의 지도자들이었고 하나의 기구에 속해 있었다.

‘유엔 안전보장이사회(The Security Council).’

늙은 주석은, 무거운 목소리로 긴급회의의 시작을 알렸다.
```

## Final English reading copy

```markdown
# Chapter 388

“Hey. Hey.”

Tap. Tap-tap.

The tip of someone’s foot nudged Wu Heixing in the side. He barely opened his eyes, and a huge shape loomed over him.

“Hngh…”

“I’ve got something urgent to take care of, so I have to leave. If anyone comes by, make up some excuse for me.”

“Hngh… hngh…”

“I poured an Advanced Potion over you, so quit pretending, punk. Keep it up, and I might call Magic Johnson over and make you moan for real. See you!”

Fwish!

After leaving behind a parting remark that made his butt ache just from hearing it, the person’s presence rapidly faded into the distance.

It was a little over ten minutes later that Wu Heixing, still sprawled spread-eagled, finally growled in a seething voice.

“Jin Taekyung…!”

His broken bones and flesh had recovered thanks to the Advanced Potion, but it could not heal the pain etched deep into his bones or his cracked pride.

*How?*

It was impossible to believe. No matter how excited he had been, how could an S-rank Hunter like him have been toyed with so thoroughly?

The fact that Jin Taekyung had seen through his martial arts was shocking enough, but for someone who took such immense pride in his own power, the shock of defeat struck even harder.

*Me? Me, of all people?*

Wu Heixing had been born with a Hunter’s fate.

Even as an infant, his potential had been recognized through an enormously expensive mana aptitude test, and his family—part of the highest echelons of the Chinese Communist Party—had spared no expense supporting him.

Vast wealth and power accumulated through corruption. Raised in the finest environment with every possible advantage, Wu Heixing awakened as an A-rank Hunter at the age of twenty. Ten years later, he achieved the remarkable feat of becoming an S-rank Hunter.

And yet…

*But why? Why was I defeated by that bangzi bastard from such a small country?*[^1]

A fierce light flashed in Wu Heixing’s eyes as he glared at the pitch-black night sky.

His gaze held anger, but also jealousy—and a trace of fear toward the power Jin Taekyung had displayed.

And those emotions were ones Wu Heixing had been sickeningly familiar with for more than a decade.

Toward the one person he could no longer find, Wu Heixing shouted.

“Was this your doing? Are you trying to torment me even after death?”

The public and the media cursed him as an incorrigible degenerate while praising him as a genius born of Zhonghua, but a tiny handful of people, Wu Heixing among them, knew the truth.

The true genius was someone else. That was why they had kept him hidden instead of letting him come to light.

“Answer me, Lei Fei!”

Lei Fei possessed not only overwhelming skill but also a noble character. To Wu Heixing, he had been an insurmountable wall.

How flustered—and delighted—had Wu Heixing been when he first heard that Lei Fei had disappeared?

But in just one week, another wall had appeared.

His name was Jin Taekyung.

“Gaaaaaaaaah!”

His roar echoed across the night, making the bushes tremble.

“That feeling… I know it well, too.”

At the quiet voice of someone who had approached without making a sound, Wu Heixing sprang to his feet like a bolt of lightning.

“Who are you?”

“I’m hurt. I thought we knew each other.”

Step.

A figure suddenly stepped out of the darkness. Wu Heixing’s eyes widened.

“You’re…?”

Beneath the faint moonlight, Lee Jungryong continued with a smile.

“It seems we have something important to discuss. What do you think?”

“...!”

* * *

Ding.

> **System**
>
> - You have finished circulating your qi!
>
> - Your realm in the Blazing Flame Divine Art has risen slightly!

By the time I gathered my qi and opened my eyes, the world outside had brightened.

As though it had been waiting for this exact moment, the Skeleton Warlord promptly opened its mouth.

- Vile human. You have finally awakened?

“I wasn’t asleep, punk.”

- You drank alcohol before a battle. Tsk, tsk.

“I’m not going to get a hangover, so shut up.”

Drinking too much caused alcohol toxins to build up, but any halfway decent internal arts master could easily purge them.

With my powerful Scorching Yang Qi, I had even less to worry about.

*Come to think of it, I really did drink a lot. I drank every last bottle of alcohol Pai Chen had flown in on her private jet.*

I had definitely gone there to stop Magic Johnson, but I had no idea how things had ended up like that.

- Human, how much longer do you intend to stay in this cramped place?

“I was planning to leave anyway.”

The clock showed five-thirty in the morning. It was about time to get ready.

After packing my things in the hotel room assigned to me as temporary lodging, I went down to the lobby and found Team Leader Choi drinking coffee.

“Oh, Team Leader.”

“...You’re out.”

A quick glance told me his eyes were hollow with exhaustion. His skin, usually flawless thanks to his meticulous self-care, looked rough.

“Did you not sleep?”

“If you were in my position, Mr. Jin, would you be able to sleep?”

“...”

Fair point.

Last night, I had received the most desperate emergency message in the world and rushed over. What I witnessed there had been nothing short of horrifying.

*“Hey, Choi. This is a drinking game. Come on, just do it once. Be cool. Right?”*

*“Pai Chen! Please, help me, Pai Chen!”*

*“Hmm… Sorry, but this is a drinking game. The king’s command is absolute. Isn’t that the rule?”*

*“Even so, a kiss? This is my first drinking game! You didn’t even explain the rules properly!”*

*“Ah, whatever, whatever. Number Two will kiss Number Three on the cheek. That’s my command.”*

*“Choi. Stay still. I don’t want to cast a binding spell on you.”*

*“This is absurd… Jin Taekyung! Jin Taekyung, over here!”*

*“Jin. Don’t interfere. I don’t want to use an attack spell on you.”*

Honestly, if I had been one minute late, it would have ended in a catastrophe.

I had been forced to chug an enormous amount of alcohol in exchange for rescuing Team Leader Choi, but I had not regretted it for a second. I had been promised a fair reward in return.

“You remember the promise you made yesterday, right? You said you’d adjust my share of the settlement.”

“...I remember. Nine to one.”

Team Leader Choi glared at me coldly.

“How could you do that in such an emergency? Are you even human?”

“Then give him one good, passionate kiss right now. Number Two is coming over.”

He might have been Number Two, but his gay stat was the highest in the world.

Team Leader Choi spotted the huge Black man just entering the lobby—Magic Johnson—and spat out the coffee he had been drinking.

“Ptooey! Please, please hide me!”

“I think it’s already too late.”

The moment I finished speaking, Magic Johnson spotted us and waved a palm the size of a pot lid.

“Hey, gays!”

Wasn’t it usually *guys*? He must have misspoken… right?

Magic Johnson approached us as Team Leader Choi and I stood there, wondering if we had heard correctly, then laughed heartily.

“Don’t make such expressions. I was just a little excited yesterday and playing around.”

“...You were really excited?”

“Ah. I suppose that’s how it sounded.”

“Watch what you say. You startled me.”

“Haha. Anyway, something came up yesterday.”

“...What came?”

“Huh? No, not that kind of coming.”

“Watch what you say. You really startled me.”

“Please, both of you, stop. I’m afraid someone will hear you.”

Team Leader Choi, wearing an utterly enlightened expression, drained the coffee that remained in his cup and turned his head.

A group of people had passed through the hotel’s main entrance and were walking toward us.

“It is time to depart, gentlemen.”

The voice of Minister of Defense Wei Penghu, who led the group, was stiff with tension.

At his signal, a military general who looked well into his later years began handing out folders one by one.

“What is this?”

“Information on the areas to which you have been assigned and the forces stationed there. Of course, we have already sent the necessary information and established communications with the people on that side. From now on, you will travel aboard the designated jets.”

Modern technology did have its conveniences.

A short while later, at the temporary airfield where we arrived behind Wei Penghu, I saw several familiar faces surrounded by tight security.

“Did you sleep well, youngsters?”

“...”

“You’re late.”

Pai Chen greeted us while stretching her arms high. Wu Heixing silently lowered his gaze, perhaps because of what had happened yesterday, while Lee Jungryong wore a strange smile.

The Skeleton Warlord, safely stored inside my Inventory, spoke in a displeased voice.

- There is something unpleasant about that human. This commander does not like him one bit.

“I agree.”

Pai Chen raised an eyebrow after hearing my mutter.

“Hm? What did you say?”

“Nothing. By the way, where is Prince Felix?”

“He left just before dawn. Apparently, a battle signal came from the area assigned to him.”

“...I see.”

Another battle had broken out less than twenty-four hours after our arrival.

At the thought of the word *war*, something suddenly clenched in one corner of my chest.

Our nationalities and upbringings were different, but the thought of people just like me being brutally slaughtered somewhere weighed heavily on my heart.

“Hey, young man.”

“Yes?”

Pai Chen stared at me for a moment, then gave my shoulder a light tap.

“Relax your shoulders. They’re so tense you won’t be able to swing your spear properly.”

“...”

“Don’t blame yourself, and don’t rush. Don’t try to take responsibility for every death.”

Responsibility.

I thought about it for a moment before answering honestly.

“...I’m not sure. I can’t say I’m very confident.”

“Well, you certainly drank yourself senseless yesterday, for someone who feels that way.”

“That was…”

“I know. I’m joking. People like us forget the burden for a little while that way. We’re lives that might die tomorrow—or even today.”

The content did not suit her bright voice at all.

The hero who had fought her way through the Great Cataclysm with her entire body raised her head and looked at the sky.

“Ah. Perfect weather for a fight.”

Then she turned and began walking lightly toward the jet, which had finished preparing for takeoff.

She left us with one quiet remark.

“Let’s all see each other alive.”

Her back disappeared inside the aircraft.

Magic Johnson gazed up at the sky for a moment with an unusually solemn expression, then abruptly opened his mouth.

“Hey, Choi.”

“Yes?”

“Relax your ass, too.”

“...”

“No, I mean relax your shoulders. Let’s see each other alive again.”

*I had a feeling his true feelings had just slipped out.*

Magic Johnson laughed heartily at Team Leader Choi’s wary gaze and boarded the aircraft after Pai Chen.

Wu Heixing followed, walking as though he were trying to escape. Finally, Lee Jungryong was left behind. He looked us both over with strange eyes.

“Both of you, take care. You can’t go dying young in a place like this—not at your age.”

*What an old man’s way of putting it. What a meaningful thing to say.*

I smiled and spoke in place of Team Leader Choi, whose face had gone rigid.

“We should. Unlike some people, dying now wouldn’t exactly be a good death for us.[^2]”

“...!”

“If you kick the bucket, I’ll make a generous condolence contribution.”

“I’ll look forward to it.”

After a brief silence, Lee Jungryong tossed out that one remark and led the Ares Guild members away.

Now only the two of us remained.

I stretched as hard as I could, then patted Team Leader Choi on the shoulder.

“Let’s go, Team Leader.”

“Yes. We should.”

“There’s nothing to be nervous about. Relax your ass.”

“...”

“...I was joking. Sorry.”

*At this rate, two jokes would be enough to kill a man.*

I was cautiously watching Team Leader Choi’s expression as I climbed aboard the aircraft when—

“Troops—attention!”

A thunderous shout erupted behind us.

Minister of Defense Wei Penghu was saluting us, his half-gray hair whipping in the wind.

The people filling the airfield followed Wei Penghu and assumed the same salute.

It was a display of respect for the heroes going off to fight for their families and friends.

Their salutes did not end until the jet door closed and the aircraft disappeared from sight as a distant speck.

*Good grief.*

After all that, there was no way my shoulders wouldn’t feel heavy.

I suddenly felt tired and leaned back against my seat.

Static crackled.

- …respond. Respond. This is…

Along with the distorted radio transmission coming from the cockpit, an alert pierced my ears.

Ding.

> **System**
>
> - Unexpected Quest generated: The Battle Situation Has Become Critical.
>
> - You cannot refuse the Quest. Arrive as quickly as possible and defeat the enemies!

“...”

*Damn it. That’s just how my life is.*

I let out a deep sigh, then shouted toward the cockpit.

“Sir, give it full throttle!”

* * *

“What about them?”

The person who spoke was an old man in his eighties. His face was covered in wrinkles and age spots. His aged body was no longer what it had been in his youth, but his eyes held even greater power than they had back then.

Even through the holographic screen, the force in the old man’s gaze could be felt. Wei Penghu swallowed hard before answering.

“They have all departed, Comrade Chairman.”

“How is the battle situation?”

“We cannot easily determine the enemy’s movements because of communication interference caused by magic and the barriers, but we are doing our best to detect their movements.”

“If the S-rank Hunters arrive…”

“With their power, they should be more than capable of turning the tide.”

“Do not jump to conclusions. Do not let your guard down for even a moment. The lives of countless people depend on our decisions.”

“Yes. I will keep that in mind.”

After the brief communication with Minister of Defense Wei Penghu ended, state chairman Xiao Yang sat alone in the vast conference room, lost in thought.

*How did things come to this?*

This was an unprecedented catastrophe since the Great Cataclysm.

Despite pouring in vast amounts of personnel and funding, they had been unable to stop the monster army centered around an Arch Lich.

He had wanted to prevent panic as much as possible, but if they delayed any longer, the opportunity might disappear forever.

That was why Xiao Yang had come here today, despite the countless objections from within the Communist Party.

“We’re ready.”

“...Connect me immediately.”

At the secretary’s words, Xiao Yang opened his closed eyes.

One by one, holographic figures began to appear above the empty seats in the vast conference room.

Fourteen people of different races and genders.

No—fifteen, including Xiao Yang.

Every one of them was the leader of a country, and they belonged to a single institution.

*The United Nations Security Council.*

The old chairman announced the beginning of the emergency meeting in a heavy voice.

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.

[^2]: A *ho-sang* is a death considered fortunate because it comes after a long, full life, usually at an advanced age.
```
