<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0386.txt",
      "sha256": "4885a393ec1de0b3d19c44efa37157f2d0a4a248f3bcbc1682322f939ee077f2",
      "bytes": 13178
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3e6ae3304fefbecce3b89818bd07b31163cd6e195ed96191bb9e4b6b17b93232",
      "bytes": 4793
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "74dd650d61ade6a33835e41833581ec23ac9c0481b9972156616363a9d61e54a",
      "bytes": 12405
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "59b9613048ce2fb970f4e2ae6bdbd4e3f7760ae97dc234cd51258f0598f529ba",
      "bytes": 23777
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "d2770f9356f099378fc00fc6cdb99de81c472fa7649d0276c4a297d527c7a4ae",
      "bytes": 3813
    },
    {
      "path": "characters/Wei Penghu.md",
      "sha256": "cbe1a4cfe004d30958ab3387194a357b7ac2ff9b6cd9d4cca2aea29d8a943c3b",
      "bytes": 607
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "93803673d7533764d0ce0fdb8712903a2765daf038e299f6f400fd6d185c5956",
      "bytes": 509
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6d7be369595d99038d6671b238dbd50de195dee261b17f1c9a19295973eab240",
      "bytes": 7717
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 14987
}
-->

# Durable State Update — Chapter 386

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 386. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 386. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 386,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 386,
    "continuity_sources": [386],
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
    "Jin Taekyung is a Supreme Peak martial artist; his exact current level, Fame, complete Titles, martial-art stages, and unassigned points remain unstated.",
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
    "Lee Jungryong has arrived at the temporary operations headquarters with Wei Penghu, and Taekyung recognizes him as a dangerous old tiger and cunning snake."
  ],
  "continuity_sources": [
    385
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "Lee Jungryong's purpose in coming to the bunker and his next interaction with Taekyung remain unresolved; Wu Heixing's interrupted attempt to draw his sword also has no outcome."
  ],
  "safe_through": 385,
  "temporary_decisions": [
    "Use the current Korean source as authoritative; the skipped range is not accepted English continuity.",
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생 and Comrade Chairman for 주석 동지.",
    "Render 반도의 빵즈 as peninsula bangzi and retain the derogatory-slur footnote.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's offensive insult exchange.",
    "Render Pai Chen, Wu Heixing, Prince Felix Alexander Louis, and William consistently, including Felix's full British title recital."
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

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 무인     | **martial artist**                               | Default term                                          |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |
| 핑핑이 | **Pingping** | Taekyung's joking guess at the name of the deceased former chairman; not established as the actual name. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 385
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 54
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Reawakened Hunter publicly classified as C-rank; leader and employer of the Peace Guild’s E-rank Gate party
- **Personality:** Calm, observant, practical, and decisive under pressure
- **Voice:** Polite and measured in ordinary conversation; clipped and commanding during combat
- **Relationships:** Hires Jin Taekyung as a porter and leads him, Im Kkeokjeong, and three veteran E-rank Hunters through an E-rank Gate

### Wei Penghu.md

# Wei Penghu (웨이펑후)

- **Safe through:** Chapter 385
- **Aliases:** None
- **Role:** Senior General and Minister of Defense at the Central Military Commission
- **Personality:** Courteous, composed, and direct in his first meeting with Jin Taekyung
- **Voice:** Formal and respectful
- **Relationships:** Meets Jin Taekyung after the Chengdu International Airport battle, brings him toward the temporary operations headquarters, and is Lei Fei's uncle; he raised Lei Fei as his own son and asks Taekyung to bring him back if found.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 385
- **Aliases:** None
- **Role:** S-rank Hunter and highly media-exposed Chinese Hunter
- **Personality:** Arrogant, volatile, status-conscious, and attention-seeking
- **Voice:** Aggressive, insulting, and indignant
- **Relationships:** Antagonizes Jin Taekyung and resents the attention Taekyung receives from Xiao Yang; rumored to be the son of a senior Communist Party official.

## Korean source

```text
＃386화



“내가 너무 늦었군. 많이들 기다렸나?”

이정룡은 모여 있는 사람들의 면면을 훑었다. 익숙한 얼굴도, 오늘 처음 보는 이들도 있었다.

대격변 당시 몇 번 마주쳤던 매직 존슨, 파이 첸, 그리고 영국의 애송이 왕자와 중국의 문제아까지.

한 사람, 한 사람과 시선이 마주칠 때마다 지하 벙커에 모인 S급 헌터들이 이정룡을 향해 먼저 인사를 건넸다.

「오랜만이야, 리. 못 본 사이에 더 매력적인 남자가 됐네. 당신을 볼 때마다 고백하고 싶어진다니까.」

“참아 주게, 매직 존슨. 난 그쪽 취향이 아니거든. 여기 있는 파이 첸이라면 모를까.”

이정룡의 천연덕스러운 대꾸에 파이 첸이 긴 머리카락을 쓸어올렸다.

「어머, 이 선생이 나한테 그런 마음이 있는 줄은 몰랐는데. 아쉽네요. 너무 늦게 알아서.」

“아쉬울 게 뭐가 있겠소. 아직 한창때인데.”

「그렇게 말해 주니까 고맙긴 한데, 젊은 친구들이 들으면 비웃어요. 늙은이들끼리 뭐 하는 짓이냐고.」

“정말 그런가?”

이정룡의 시선에 우헤이싱이 다급하게 손을 내저었다.

「아, 아닙니다. 이 선생님. 그럴 리가 있겠습니까.」

“자네 얘기는 많이 들었지. 재능이 뛰어나고, 음. 매사에 솔직한 청년이라고.”

「가, 감사합니다.」

우헤이싱이 황송하다는 듯한 얼굴로 고개를 숙였다.

평소에는 혐한 기질에 한국인을 비하하는 뜻인 빵즈를 입에 달고 사는 그였지만, 감히 이정룡의 앞에서 그런 모습을 보일 만한 담력은 없었다.

우헤이싱의 목덜미에서 식은땀 한 방울이 또르르 굴러떨어졌다.

「이야기를 듣긴 했지만 정말 오실 줄은 몰랐습니다.」

“당연히 와야지. 이웃이 어려우면 돕고 살아야 하는 것 아닌가.”

「이 선생님을 만나 뵙게 되어 영광입니다.」

대격변이 낳은 영웅들인 매직 존슨과 파이 첸조차 이정룡에 비할 수는 없다.

21세기의 예수, 전 세계의 구원자라 불리는 천태민의 의형제이자 바로 그 아레스 길드의 실질적인 수장이니까.

세계에서 손꼽히는 막강한 길드. 그리고 S급 헌터 중에서도 세 손가락 안에 드는 강자. 이정룡.

그와 마주한다면 마땅한 경의를 표해야 한다.

안하무인인 우헤이싱도, 고귀한 혈통을 지닌 왕족도 예외는 아니었다.

“만나서 반갑소. 반갑습니다, 정룡 리.”

“아, 자네가 바로 그 왕자로군.”

「무엄하…….」

손을 들어 비서의 말을 막은 필릭스 왕자가 기품 있게 고개를 살짝 숙였다.

“필릭스. 필릭스라고 부르면 되오. 됩니다.”

통역기를 거친 어색한 한국어와 애매한 말투.

하지만 이것으로 영국 왕위 계승 서열 3위, 필릭스 알렉산더 루이는 다른 이들과 이정룡의 차이를 분명히 했다. 무려 ‘왕자 전하’라는 호칭을 생략하게 해 준 것이다.

물론 이정룡은 신경조차 쓰지 않았다.

‘그래 봤자 애송이들.’

이정룡이 인정하는 것은 매직 존슨과 파이 첸까지다.

성격이야 어쨌건 세간에서는 천재라 불리는 우헤이싱과 필릭스 왕자도 그의 눈에는 이제 막 걷기 시작한 햇병아리에 불과했다.

그리고…… 정작 이정룡의 신경을 거스르는 이들은 따로 있다.

‘평화 길드.’

이정룡의 시선이 한쪽을 향했다. 말없이 서 있는 두 사람을 바라보는 그의 입가에 진한 미소가 맺혔다.

“요즘 들어 자주 보게 되는군. 두 사람 모두 잘 지냈나?”

이정룡이 건넨 인사에, 서로를 바라본 진태경과 최민우가 어깨를 으쓱했다.

“별로.”

“그다지.”

“……?”

뭐지?

이정룡은 자신도 모르게 멈칫했다.

마지막으로 본 것은 불과 한 달도 되지 않은 짧은 시간. 그러나 그를 대하는 두 사람의 태도에는 큰 변화가 있었다.

‘적의(敵意).’

바로 그것이다. 놈들에게서는 예전처럼 뚜렷한 적의와 경계심이 느껴지지 않았다.

담담하기 그지없는 두 사람을 바라보던 이정룡은 곧 그 이유를 깨달을 수 있었다.

‘강해졌다. 전과는 비교할 수 없을 정도로.’

틀림없었다. 도대체 무슨 수로 단기간에 이렇게 성장했는지 궁금해질 만큼, 최민우에게서 느껴지는 기운은 전에 비해 훨씬 더 크고, 정제되어 있었다.

그리고 다른 한 사람, 진태경은.

‘……이건.’

피부와 육감을 통해 느껴졌다. 진태경의 전신에 갈무리된 강대한 기운이. 깊게 가라앉은 놈의 눈동자가.

이것이 의미하는 바는 하나뿐이다.

‘벽을, 넘었다.’

뒤통수를 한 대 얻어맞은 듯한 충격. 이정룡은 동요를 드러내지 않기 위해 안간힘을 써야 했다.

‘도대체 어떻게?’

이전에도 진태경은 분명 강자였다. 어쩌면 전 세계에 존재하는 수많은 A급 헌터들의 머리 위에 선 존재였을 것이다.

단독으로 네임드 몬스터를 둘이나 처치할 정도였으니, 사람들과 언론이 새로운 S급 헌터의 탄생이라며 떠드는 것은 당연했다.

하지만 이정룡은 알고 있었다. 진태경이 아직 ‘벽’을 넘지 못했다는 것을. 녀석의 앞을 가로막은 벽을 넘어 진정한 강자가 되기까지는 아주 오랜 시간이 필요하리라는 사실을.

그런데…….

‘이런 말도 안 되는 일이 벌어지다니.’

놀라움이라는 감정으로 표현할 수 있는 일이 아니다. 자신을 향한 진태경의 덤덤한 눈빛을 마주한 이정룡은, 오랫동안 잊고 있던 감정을 떠올렸다.

불안. 초조.

그건 이정룡이 아레스 길드를 온전히 손에 넣은 후 처음으로 느끼는 불안감이었다.

몇 달 전만 하더라도 그저 우습고 거슬리던 존재. 그런 놈이 자신에게 불안과 초조라는 감정을 일깨워 주었다.

‘이놈…….’

이정룡의 입가에 맺혀 있던 웃음은 씻은 듯이 사라졌다. 굳은 얼굴을 한 그를 웨이펑후가 의아하게 바라봤다.

「이 선생? 무슨 문제라도 있습니까?」

“……별일 아니오.”

「흠. 그럼 이제 회의를 시작해도 되겠습니까?」

말없이 고개를 끄덕이는 이정룡의 시선은 시종일관 한 사람에게 고정되어 있었다.

의자 등받이에 비스듬히 몸을 기댄 청년, 진태경이 혼잣말처럼 중얼거렸다.

“글쎄, 충분히 별일 같아 보이는데.”

“……!”

“뭐, 아니면 말고.”

이정룡은 자신도 모르게 주먹을 힘껏 움켜쥐었다.



* * *



지하 벙커에서 이루어진 회의는 오랫동안 이어졌다.

지난 일주일간 최소 수십 만의 사상자를 발생시킨 몬스터 웨이브다. 그 자체만으로도 이미 엄청난 천재지변이었고, 확실한 전시 상황이었으니 신중에 신중을 기하는 것은 당연했다.

「하여, 오군(五軍)으로 나누어 적들을 압박해 나가는 것이…….」

심각한 얼굴로 말을 이어 나가려는 웨이펑후의 말을 누군가가 가로막았다.

「이보시오. 국방부장 동지.」

「말씀하시오. 랴오 상장.」

정복에 온갖 훈장을 주렁주렁 매단 장년인, 랴오 상장이라 불린 그가 수염을 쓰다듬으며 입을 열었다.

「내 국방부장의 말을 듣자 하니, 너무 답답해서 말이오. 그렇게 지지부진해서야 어느 세월에 저 몬스터 놈들을 처리하겠소?」

이야…….

말투가 보통 띠꺼운 게 아니다. 주석의 오른팔이자 군부 최고위 실권자인 웨이펑후에게 저런 식으로 말을 할 수 있다니.

마치 내 의문을 읽은 것처럼 최 팀장이 메시지 마법을 보냈다.

- 공산당도 각각 파벌이 있습니다. 랴오 상장은 조부 시절부터 공산당 최대 계파인 태자당(太子党)의 성골 출신으로, 샤오 주석과 웨이펑후 국방부장이 속해 있는 상하이방(上海帮)과는 경쟁 관계입니다.

- 태자당이랑 상, 뭐요?

- ……굳이 따지자면 태자당이 1번이고, 상하이방이 2번이라는 소립니다.

- 아.

지금까지 공산당 하면 무조건 일당 체제인 줄 알았는데, 자기네들끼리도 열심히 치고받고 싸우는 모양이다.

- 그런데 그래도 됩니까? 샤오 주석이 손가락으로 딱 가리키면서 저놈은 해로운 놈이다. 한마디 하면 천안문 광장에서 참수당하는 거 아니에요?

- 되니까 하죠.

- ……아니, 뭐. 그렇게 말씀하시니까 할 말이 없네.

- 파벌끼리 합의를 본 겁니다. 대격변 당시 태자당 출신 주석이 하도 실수를 많이 해서 계속 정권을 잡기에는 눈치가 보였던 거죠.

- 아, 핑핑이?

- 예. 핑핑이.

그놈의 대격변이 참 여러 가지를 바꿔 놨구나.

내가 최 팀장으로부터 그런 설명을 듣고 있는 사이, 태자당 성골 유스 출신이라는 랴오 상장은 기똥찬 제안을 내놓았다.

「핵을 씁시다.」

「……?」

「……?」

「샤오 주석에게 정식으로 요청해서, 핵 수십 발을 사천 전역에 날려 버리잔 말입니다. 그럼 깔끔하게 해결될 것 아니오?」

「…….」

「…….」

저런 미친 핵쟁이 새끼를 봤나.

나를 포함한 모두가 어이없는 얼굴로 서로를 바라보았다.

그중에서도 특히 웨이펑후 국방부장의 표정이 압권이다. 그는 권총이 마려운 표정으로 대답했다.

「기각하오.」

「어째서! 지금 상하이방이 아니라고 무시하는 거요!」

「말이 되는 소릴 하시오. 말이 되는 소릴! 그렇게 되면 아직 생존해 있거나 피해를 입지 않은 인민들은! 황폐해지는 국토는 어쩔 거요!」

「대를 위한 소의 희생은 어쩔 수 없소!」

다른 건 모르겠고 그냥 소 대가리 같은데.

조용히 듣고 있던 매직 존슨이 굵은 목소리로 불쑥 입을 열었다.

「핵 공격이 성공했을 때의 피해도 피해지만, 공간 이동 마법으로 핵탄두를 이동시키면 어쩌려고? 예를 들면 북경이라거나.」

「그건 대마법사인 당신이 있으니까…….」

「나? 상대는 보통 리치가 아니야. 만약 아크 리치라는 놈이 나보다 마법이 뛰어나다면, 그땐 정말 돌이킬 수 없는 참사가 일어나. 이미 대격변 초기에도 비슷한 일이 몇 번 있었잖아?」

「그, 그래도…… 이 정도 희생쯤은…….」

「헤이. 머더 퍼커.」

쾅!

깜짝이야. 자리를 박차고 일어난 매직 존슨이 구릿빛 근육을 꿈틀거렸다.

「그만해. 나, 동양인 남자도 좋아하니까. 벌을 내려 줄 수도 있어.」

「……!」

「……!」

지금까지 들어 본 협박 중에 제일 무섭다.

얼굴이 새파랗게 질린 랴오 상장이 구원을 바라는 눈빛으로 주위를 둘러봤지만, 같은 계파에 속해 있는 것으로 짐작되는 관료들은 물론이고 최후의 보루인 우헤이싱도 그의 시선을 외면했다.

‘이게 이렇게 해결되네.’

상대는 미국의 국민 영웅이자 국민 게이.

모두가 매직 존슨이 좋아하는 동양인 남자가 되기 싫어서 안간힘을 쓰는 모양이었다.

물론 랴오 상장이 너무 개소리를 지껄인 것도 크게 한몫했다.

「그만하시오, 두 분 다. 특히 랴오 상장은 턱도 없는 소리 그만하시고.」

짱깨를 진압한 중국인, 웨이펑후의 주도하에 이후 회의는 빠르게 진행되었다.

앞서 나온 의견들을 종합, 설전을 거친 끝에 모두의 동의를 얻어 낸 웨이펑후가 지친 얼굴로 입을 열었다.

「여기 계신 S급 헌터 여섯 분을 여섯 개 방면으로 나누어 배치하겠소. 정식 편제에 따라 방면마다 육, 공군 세 개 사단, 그리고 공안 무력부의 헌터를 파견할 거요.」

중국 세 개 사단에 공안 무력부라.

정확히 그 숫자가 몇이나 될지는 몰라도, 물량 하나만큼은 어마어마할 것이다.

보유한 헌터의 숫자로 따지면 늘 첫째, 둘째를 다투는 중국 아닌가.

‘물론 저쪽도 만만치 않지만.’

피해 사상자 추정치만 수십만 명이다.

아크 리치가 죽은 자들을 언데드로 부활시켰다면…… 그야말로 아득한 숫자의 적들이 우리를 기다리고 있을 것이다.

「이것으로 회의를 끝마치겠소. 여러분들께서는 속히 이동하시오.」

정확한 숫자와 편제를 서면으로 알려 준다는 웨이펑후의 말과 함께, 사람들이 자리에서 일어난 바로 그때였다.

- 잠깐 나 좀 보지.

귓가를 파고드는 누군가의 목소리. 그건 메시지 마법이 아닌, 틀림없는 전음(傳音)이었다.
```

## Final English reading copy

```markdown
# Chapter 386

“I’m too late. Have you all been waiting long?”

Lee Jungryong swept his gaze over the assembled people. Some faces were familiar, while others were strangers he was seeing for the first time today.

Magic Johnson and Pai Chen, whom he had encountered several times during the Great Cataclysm. The young British prince. And China’s problem child.

Each time his eyes met someone’s, the S-rank Hunters gathered in the underground bunker greeted Lee Jungryong first.

“It’s been a while, Lee. You’ve become an even more attractive man since we last met. Every time I see you, I feel like confessing my love.”

“Please restrain yourself, Magic Johnson. You’re not my type. Though I might make an exception for Pai Chen over there.”

At Lee Jungryong’s shameless reply, Pai Chen swept her long hair back.

“Oh my. I didn’t realize Mr. Lee had feelings for me. What a shame. I found out too late.”

“What’s there to regret? You’re still in your prime.”

“Thank you for saying that, but if young people hear you, they’ll laugh. They’ll ask what old people like us think we’re doing.”

“Is that really how it is?”

At Lee Jungryong’s gaze, Wu Heixing hurriedly waved his hands.

“Oh, no, Mr. Lee. How could that possibly be?”

“I’ve heard a lot about you. You’re remarkably talented and… a young man who’s honest about everything, I hear.”

“T-Thank you.”

Wu Heixing bowed his head, looking deeply honored.

Normally, he was so hostile toward Korea that he constantly spat out the word *bangzi*, an insult for Koreans. But he lacked the nerve to show that side of himself in front of Lee Jungryong.

A bead of cold sweat rolled down the back of Wu Heixing’s neck.

“I’d heard you were coming, but I never thought you really would.”

“Of course I had to come. When your neighbor is in trouble, shouldn’t you help them?”

“It’s an honor to meet you, Mr. Lee.”

Even Magic Johnson and Pai Chen, heroes born from the Great Cataclysm, could not compare with Lee Jungryong.

He was the sworn brother of Cheon Taemin, called the Jesus of the twenty-first century and the savior of the world. He was also the real leader of that Ares Guild.

A powerful Guild counted among the strongest in the world. And a man ranked among the top three strongest S-rank Hunters.

Lee Jungryong.

Anyone who faced him had to show the proper respect.

Wu Heixing, arrogant as he was, was no exception. Neither was royalty of noble blood.

“Pleased to meet you. A pleasure to meet you, Jungryong Lee.”

“Ah. So you’re that prince.”

“How dare—”

Prince Felix raised a hand to stop his secretary and gave a dignified little bow.

“Felix. You may call me Felix. You may.”

The Korean produced through the translation device was awkward, and his speech level was oddly ambiguous.

But with that, Felix Alexander Louis—third in line to the British throne—made the difference between Lee Jungryong and everyone else perfectly clear. He had actually allowed Lee Jungryong to omit the title *Your Royal Highness*.

Of course, Lee Jungryong did not care in the slightest.

*They’re all just brats.*

The only ones Lee Jungryong acknowledged were Magic Johnson and Pai Chen.

Whatever their personalities, Wu Heixing and Prince Felix were considered geniuses by the public. But in Lee Jungryong’s eyes, they were nothing more than chicks that had only just learned to walk.

And…

The people who truly irritated Lee Jungryong were elsewhere.

*The Peace Guild.*

Lee Jungryong’s gaze turned in one direction. A deep smile formed around his mouth as he looked at the two people standing there in silence.

“I’ve been seeing you two quite often lately. Have you both been well?”

At Lee Jungryong’s greeting, Jin Taekyung and Choi Minwoo looked at each other and shrugged.

“Not really.”

“Not particularly.”

“…?”

What?

Lee Jungryong faltered without realizing it.

It had been less than a month since he had last seen them. Yet there had been a great change in the way the two men treated him.

*Hostility.*

That was it.

The obvious hostility and wariness he had felt from them before were no longer there.

As Lee Jungryong looked at the two men, who were as calm as could be, he soon understood why.

*They’ve grown stronger. Incomparable to before.*

There was no doubt about it. Choi Minwoo’s energy was far greater and more refined than before—so much so that Lee Jungryong wondered how he could have grown this much in such a short time.

And the other man, Jin Taekyung…

*…What is this?*

He could feel it through his skin and sixth sense. The tremendous energy gathered throughout Jin Taekyung’s body. The deep, still look in his eyes.

There was only one meaning behind it.

*He crossed the wall.*

The shock struck Lee Jungryong as though someone had hit him in the back of the head. He had to struggle with all his might not to show his agitation.

*How?*

Jin Taekyung had already been a powerful man. He might even have stood above the countless A-rank Hunters in the world.

After all, he had defeated two named monsters alone. It was only natural that people and the media had been loudly proclaiming the birth of a new S-rank Hunter.

But Lee Jungryong knew the truth.

Jin Taekyung had not yet crossed the wall.

He knew it would take a very long time for the man to climb over the wall blocking his path and become a true powerhouse.

And yet…

*How could something this absurd happen?*

This was not something that could be expressed as mere surprise.

When Lee Jungryong met Jin Taekyung’s impassive gaze, he remembered an emotion he had forgotten long ago.

Anxiety. Impatience.

It was the first time Lee Jungryong had felt such unease since taking complete control of the Ares Guild.

Only a few months ago, Jin Taekyung had been nothing more than an amusing and irritating presence.

Yet that man had awakened feelings of anxiety and impatience within him.

*You…*

The smile on Lee Jungryong’s lips vanished as though it had been washed away. Wei Penghu stared at him in puzzlement.

“Mr. Lee? Is something wrong?”

“…It’s nothing.”

“Hmm. Then may we begin the meeting?”

Lee Jungryong nodded silently, his gaze fixed on one person the entire time.

Leaning diagonally against the back of his chair, the young man named Jin Taekyung muttered as if to himself,

“Well, it certainly looks like something to me.”

“…!”

“Never mind, then.”

Without realizing it, Lee Jungryong clenched his fists tightly.

* * *

The meeting in the underground bunker continued for a long time.

The monster wave had produced at least hundreds of thousands of casualties over the past week. It was already a massive natural catastrophe in its own right, and the situation was unquestionably one of war. Naturally, they had to proceed with the utmost caution.

“Accordingly, we should divide our forces into five armies and pressure the enemy…”

Someone interrupted Wei Penghu as he continued speaking with a serious expression.

“Comrade Minister of Defense.”

“Speak, Senior General Liao.”

The middle-aged man known as Senior General Liao wore a uniform covered in medals. He stroked his beard before opening his mouth.

“Listening to the Minister of Defense, I find myself so frustrated that I have to speak. At this rate, how long will it take us to deal with those monsters?”

*Wow…*

His tone was unbelievably obnoxious.

He was speaking that way to Wei Penghu—the Chairman’s right-hand man and the military’s highest-ranking power broker.

As if he had read my question, Team Leader Choi sent me a Message Spell.

- The Communist Party has factions too. Senior General Liao is a pure-blooded member of the Princelings, the Communist Party’s largest faction, going back to his grandfather’s generation. They’re rivals of the Shanghai clique, which Chairman Xiao and Minister of Defense Wei Penghu belong to.

- The Princelings and Shang… what?

- …If we’re being precise, it means the Princelings are number one and the Shanghai clique is number two.

- Ah.

Until now, I had assumed that the Communist Party operated under a strict one-party system. Apparently, they fought each other tooth and nail too.

- But is that allowed? If Chairman Xiao simply points at someone and says, “That man is dangerous,” and gives the order, wouldn’t that person be beheaded in Tiananmen Square?

- They do it because they’re allowed to.

- …Right. When you put it that way, I don’t have much to say.

- The factions reached an agreement. During the Great Cataclysm, the Chairman from the Princelings made so many mistakes that they felt awkward about continuing to hold power.

- Ah. Pingping?

- Yes. Pingping.

That damn Great Cataclysm had changed a lot of things.

While I was listening to Team Leader Choi’s explanation, Senior General Liao—who apparently came from the Princelings’ pure-blooded younger generation—made an absolutely brilliant proposal.

“Let’s use nuclear weapons.”

“…”

“…”

“Let’s formally request it from Chairman Xiao and fire dozens of nuclear weapons across all of Sichuan. Wouldn’t that solve everything cleanly?”

“…”

“…”

What a lunatic nuclear-happy bastard.

Everyone, myself included, looked at each other with dumbfounded expressions.

Wei Penghu’s expression was especially spectacular. He answered with the face of a man who desperately wanted a pistol.

“Rejected.”

“Why? Are you ignoring me because I’m not part of the Shanghai clique?”

“Say something that makes sense. Something that makes sense! If we do that, what happens to the people who are still alive or haven’t been harmed? What about the land we leave barren?”

“Sacrificing the few for the sake of the many is unavoidable!”

Forget the rest—he just sounded like an ox head to me.[^1]

[^1]: The Korean word *so* can mean both “the few” in the general’s maxim and “ox,” turning his solemn justification into an insult.

Magic Johnson, who had been listening quietly, suddenly spoke in his deep voice.

“The damage from a successful nuclear attack is bad enough, but what are you going to do if someone uses spatial teleportation magic to move the nuclear warheads? To Beijing, for example.”

“That’s why we have an Archmage like you…”

“Me? Our opponent isn’t an ordinary Lich. If this Arch Lich is more skilled in magic than I am, then it will cause an irreversible catastrophe. Something similar already happened several times during the early days of the Great Cataclysm, remember?”

“B-But even so… sacrifices on this scale…”

“Hey. Motherfucker.”

Bang!

I nearly jumped out of my skin. Magic Johnson had shot to his feet, and his bronze-colored muscles rippled.

“Knock it off. I like Asian men too, you know. I might punish you.”

“…”

“…”

That was the scariest threat I had ever heard.

Senior General Liao’s face turned deathly pale as he looked around for help. But the officials who appeared to belong to his faction avoided his gaze. Even Wu Heixing, the last line of defense, looked away.

*So this is how it gets resolved.*

The opponent was an American national hero and a national gay icon.

Everyone seemed desperate not to become the Asian man Magic Johnson liked.

Of course, the fact that Senior General Liao had been spouting such ridiculous bullshit also played a major role.

“Enough, both of you. And especially Senior General Liao—stop talking nonsense.”

Under Wei Penghu’s leadership—a Chinese man who had just subdued the chink—the meeting moved forward quickly.

After gathering the opinions that had been raised and exchanging heated arguments, Wei Penghu finally won everyone’s agreement. He spoke with a tired expression.

“We will divide the six S-rank Hunters present here among six fronts. According to the official organization, each front will receive three Army and Air Force divisions, along with Hunters from the Public Security Armed Forces.”

Three Chinese divisions, along with the Public Security Armed Forces.

I had no idea exactly how many that meant, but their sheer numbers would be enormous.

China was always fighting for first or second place when it came to the number of Hunters it possessed.

*Of course, the other side isn’t exactly easy either.*

The casualty estimates alone were in the hundreds of thousands.

If the Arch Lich had resurrected the dead as undead…

Then an unimaginable number of enemies would be waiting for us.

“This concludes the meeting. Please move out as soon as possible.”

Just as everyone rose from their seats after Wei Penghu said he would provide the exact numbers and formations in writing, a voice suddenly reached my ear.

- Come see me for a moment.

It was not a Message Spell, but unmistakably Sound Transmission.
```
