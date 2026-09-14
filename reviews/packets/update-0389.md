<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0389.txt",
      "sha256": "d3b89f228a1559fb1d8cf693f875795d806377a55890184720c7c542fce2d61d",
      "bytes": 12860
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5bc49553cfe879e98c58530cbef8df5cb163bf2512bbe896afeef803d6d6bf17",
      "bytes": 5542
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4e2c653bbfa7a8c7a41b669965c0e635a49ee04904505335db2e2b7c94472bc0",
      "bytes": 13289
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2e9fdff651d04c1d8086b616db1dbbc06064e23f7a39971285d4b78c8772e00b",
      "bytes": 23802
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "a31900fd93fe7224ba701f7efc71bd2ab1f21fd86d864fb145bb7f2f122d0962",
      "bytes": 610
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3da879d44982aa67333c27e06d764e9c2ca8a1121bb07fcd524185ac35129f0b",
      "bytes": 10241
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 15863
}
-->

# Durable State Update — Chapter 389

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 389. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 389. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 389,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 389,
    "continuity_sources": [389],
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
    "Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission; he raised his missing nephew Lei Fei as his own son.",
    "Xiao Yang is Chairman of the Central Military Commission, General Secretary, and state chairman of the People's Republic of China, and retains full authority over the crisis response.",
    "Team Leader Choi trusts Taekyung, was rescued by him from a drinking-game predicament, and agreed to adjust Taekyung's settlement share to nine-to-one.",
    "The six S-rank Hunters are assigned to six fronts and have departed by designated jets; Prince Felix left before dawn after receiving a battle signal.",
    "Magic Johnson is an S-rank Hunter, one of three Archmages worldwide, and a combat-specialized War Mage.",
    "Pai Chen is an S-rank Hunter, Great Cataclysm hero, and former romance-film actress who appears much younger than her actual age.",
    "Wu Heixing is an S-rank Hunter from a powerful Chinese Communist Party family; he is arrogant, volatile, status-conscious, and regards the missing Lei Fei as an insurmountable rival.",
    "Prince Felix Alexander Louis is a British prince, third in line to the throne, and holds multiple senior British titles; William serves as his formal attendant.",
    "The Sichuan Tang Clan was devastated by Dark Heaven, owes Taekyung's group a debt, and is considering relocation.",
    "The Chengdu International Airport attack involved an undead army controlled by three incomplete Arch Liches, all of whom Taekyung destroyed.",
    "The Skeleton Warlord absorbed the death energy of the remaining two Arch Liches and became much stronger, but the persistence and full extent of that increase remain unknown.",
    "Dark Heaven's agents, purpose, and connection to the hidden transport formation remain unresolved.",
    "Ae-hyang appears to serve an unidentified superior after a sinister red light entered her eyes, and the Sichuan Governor's false memorial remains unresolved.",
    "Lee Jungryong is the practical leader of Ares Guild and one of the world's top three S-rank Hunters; he recognizes Choi Minwoo's growth and that Jin Taekyung has crossed the wall.",
    "Wu Heixing used Sound Transmission and possesses martial-arts knowledge; Taekyung defeated him after he attacked, taking his Supreme Potion and leaving him with an Advanced Potion.",
    "An unrefusable Unexpected Quest, The Battle Situation Has Become Critical, orders Taekyung to reach the battlefield quickly and defeat the enemies.",
    "Xiao Yang has convened an emergency meeting of the fifteen leaders of the United Nations Security Council because the Arch Lich-centered monster army has overwhelmed China's response; magic interference and barriers obscure enemy movements."
  ],
  "continuity_sources": [
    388
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "The subject and consequences of Lee Jungryong's discussion with Wu Heixing, Wu Heixing's reason for sending the Sound Transmission, and the outcome of the battlefield emergency remain unresolved."
  ],
  "safe_through": 388,
  "temporary_decisions": [
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생 and Comrade Chairman for 주석 동지.",
    "Render 반도의 빵즈 as peninsula bangzi and retain the derogatory-slur footnote.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's jokes.",
    "Render established names and titles consistently, including Pai Chen, Wu Heixing, Prince Felix Alexander Louis, William, Senior General Liao, the Princelings, and the Shanghai clique; use Sound Transmission, Sword Force, Advanced Potion, and Supreme Potion here.",
    "Render 다급해진 전황 as The Battle Situation Has Become Critical and 유엔 안전보장이사회 as United Nations Security Council."
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
| 다급해진 전황 | **The Battle Situation Has Become Critical** | Name of the unrefusable Unexpected Quest generated aboard the departing jet. |
| 유엔 안전보장이사회 | **United Nations Security Council** | International body whose fifteen national leaders join Xiao Yang's emergency meeting. |

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
| 매직 존슨 | 최 팀장 | peer_ally_to_team_leader | Choi | casual-teasing | Magic Johnson repeatedly addresses Team Leader Choi by surname while joking with him. |
| 파이 첸 | 진태경 | senior_s_rank_hunter_to_younger_ally | young man | familiar-but-caring | Pai Chen uses a familiar senior-to-junior address while advising Taekyung before deployment. |
| 진태경 | 아저씨 | passenger_to_pilot | Sir | casual-urgent | Taekyung addresses the pilot informally while demanding full throttle. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 철수     | **Cheol Soo**      |
| 이정룡    | **Lee Jungryong** |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 살기     | **killing intent**                               |                                                       |
| 가주     | **Family Head**                              |
| 극양                        | **Extreme Yang**      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 염화일로 | **Flamefire Path** | Named fire-based movement technique used by Jin Taekyung. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 388
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist who has crossed the wall; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 388
- **Aliases:** None
- **Role:** S-rank Hunter and highly media-exposed Chinese Hunter
- **Personality:** Arrogant, volatile, status-conscious, and attention-seeking
- **Voice:** Aggressive, insulting, and indignant
- **Relationships:** Antagonizes Jin Taekyung and resents the attention Taekyung receives from Xiao Yang; regards Lei Fei as an insurmountable rival and was both panicked and delighted when Lei disappeared; rumored to be the son of a senior Communist Party official.

## Korean source

```text
＃389화



한파가 주춤한 어느 날이었다.

비로소 수능에서 해방된 수험생들은 재수를 준비하거나 놀기 바빴고, 직장인들은 눈 밑에 짙은 다크서클을 드리운 채 대중교통에 몸을 실었다.

그렇게 여느 때와 같은 평화로운 일상 속에서, 그 누구도 예상치 못한 폭탄이 떨어졌다.



[긴급 속보 - 유엔 안전보장이사회 중대 발표]



30분 남짓 길이의 영상은 무거운 눈빛으로 카메라를 응시하던 샤오 양 주석의 한 마디로 시작되었다.

「저는 중화인민공화국의 9대 국가주석이자 유엔 안전보장이사회의 일원으로서, 쓰촨성에서 벌어진 대규모 몬스터 웨이브를 말씀드리고자 이 자리에 섰습니다.」

전 세계의 이목을 집중시키고, 아시아 전체를 뒤흔들 폭탄이었다.



* * *



하루, 이틀, 사흘. 나흘이 지난 후에도 사태는 진정되지 않았다.

대격변 이후 수많은 사건 사고가 있었지만, 이번에 쓰촨성에서 벌어진 몬스터 웨이브는 유례를 찾아볼 수 없을 정도의 규모였다.

샤오 양 중국 주석은 공식 계엄령을 선포했고, 유엔 안전보장이사회의 승인하에 평화 유지군이 전선에 투입되었다.

전 세계의 이목이 집중된 상황.

그중에서도 특히 촉각을 곤두세우는 것은 중국과 인접한 아시아의 국가들이었다.

대한민국 역시 예외는 아니었다. 오늘도 국내 최대 포럼 사이트의 헌터 이슈란은 숯불 위 가마솥처럼 들끓고 있었다.



지금까지의 상황 요약해 준다.



이 중에서 안보리 중대 발표 영상 안 본 놈은 없겠지? 혹시 있으면 나가 뒤져야 됨. 이거 진짜 비상 상황임. 북쪽 수령 놈도 이미 아이튜브로 다 보고 여기 게시판도 눈팅 하고 있을 듯.

아무튼 지들 목숨 걸린 일까지 요약해 달라는 벌레 새1끼들 하도 많길래 참다 참다 쓴다.

1. 쓰촨성에서 원인 불명의 대규모 웨이브 발생. 현재 추정 사상자만 최소 30만.

물론 일주일 전 이야기고 지금은 비교할 수도 없겠지. 사실상 통계가 불가능하다고 봄.

2. 중국 정부가 나섰지만 생각했던 것보다 규모가 미쳤음.

아크 리치라는 놈을 중심으로 최소 수만에 달하는 몬스터 군단 결집.

인민해방군, 공군 개 털리고 공안 무력부 헌터들도 2천 명 넘게 실종(마법 방해로 통신 두절, 인공위성 감시 무력화돼서 생존 여부도 확인 못 함.)

3. 중국 정부가 비밀리에 몇몇 국가에 연락, 사태를 조속히 진압하기 위해 몇몇 S급 헌터들 고용. 이틀 전에 UN 평화 유지군까지 전선 투입해서 분전하는 중.

전투 현황은 안보리에서 업데이트하고 있으니까 관심 있는 놈은 여기 들어가 봐라.

(주소 첨부.)

아래부터는 내 개인적인 생각이니까 읽지 않아도 별 상관없음.

4. 정신머리 똑바로 박힌 사람들은 알겠지만, 지금 보통 심각한 상황이 아니다. 특히 중국 본토는 생지옥임.

쓸 만한 헌터들 끌어다가 전선에 투입하는 통에 관리가 소홀해진 다른 게이트 마력 수치도 불안하고, 모든 방면에서 초인플레이션 현상 일어나고 있음.

이게 진짜 무서운 게, 만약 전선 무너지고 몬스터 군단이 사천 밖으로 진격하게 되면…… 그 뒤는 상상에 맡긴다.

5. 그러니까 다들 ㅈ 되기 전에 마트 가서 비상식량 사 놔라. 물론 사재기로 부당이익 취하란 소리는 아님.

6. 이대로 끝내기에는 아쉬워서 국뽕 추가함.

우리의 시벌좌랑 아레스 길드 정 드래곤이 전선에서 활약 중이란다. 지금까지 빨던 대로 열심히 빨아라.

진짜 끗.



올라온 지 몇 시간 만에 조회수 10만을 돌파한 해당 게시글은 현 상황을 예의주시하고 있던 네티즌들의 댓글로 불타올랐다.



(Best댓글) 글 내용대로 심각한 상황은 맞는데, 글 작성자가 너무 분위기 쎄게 잡은 것도 있음ㅋㅋ S급 헌터들에 일반 헌터만 10만 명 참전했다는데 뭐가 그리 걱정임. 그리고 군대는 놀고 있냐?

└ ㅇㅇ걔들 지금 정비대에서 놀고 있음.

└ ……?

└ 뉴스 못 봤냐. 이번에 중국군 장비 죄다 고장 나서 최대 규모 군납 비리 드러난 거. 최소 수십조 원 규모라고 함. 발 묶인 사단이 한두 개가 아니라더라.

└ 어, 이거 어디서 많이 들어 본 얘기 같은데.

└ 제발 수통 좀 바꿔 줘라. 이 시팔 샛기들아. 작년에 전역했는데 왜 수통에서 아직도 노르망디 물맛이 나냐. 한 모금 마시면 내 이름이 김철수인지 제임스인지 헷갈리더라.

└ 김 상병님. 오늘 석식 명태 순살 조림입니다.

└ 안 먹어 ㅅㅂ

└ 그나저나 장비 고장 때문에 군대 발 묶인 것도 문제긴 한데, 걔들이야 뭐 남아도는 게 병력이라 ㄱㅊ. 어차피 몬스터한테 실질적인 타격을 줄 수 있는 건 헌터들이니까. 사실 그거 말고 더 큰 문제는 따로 있음.

└ 뭔데?

└ 몬스터 개체 수 10만 뚫음.

└ ??

└ ?????

└ 무슨 10만이야 ㅅㅂ; 개소리하지마.

└ 개소리가 아니라 유엔 안보리에서 발표한 오피셜임. 게시글 링크 타고 가서 확인해 봐라. 5분 전에 떴다.

└ 와…… 시발.

└ 윗 댓글 반응 보니까 진짠가 보네 ㅁㅊ;

└ 아니. 그냥 죄다 영어라 뭔 소린지 몰라서 그런 건데. 지금 가글 번역기 돌리고 있음.

└ 미친놈인가.

└ 야 근데 진짜 몬스터 10만 뚫었으면 큰일 난 거 아니냐. 지금까지 일어난 몬스터 웨이브 최대 규모라고 해 봐야 천 마리 안 넘었던 것 같은데;

└ 당연히 이번 웨이브도 초기에는 이 정도 규모 아니었지. 근데 저쪽에 아크 리치가 있는 게 문제야. 그냥 리치만 나타나도 큰 사건인데, 쟤는 학계에도 알려지지 않은 최상위 네임드 몬스터임. 사실상 현재 싸우는 몬스터들 대부분은 아크 리치가 부활시킨 언데드라고 해야 맞다.

└ 아크 리치 : “계왕권 100배.”

└ 그럼 아크 리치만 죽이면 되는 거 아님? 몬스터 대부분이 언데드면 조종자만 죽이면 끝나잖아.

└ ???????

└ 아크 리치를 누가 어떻게 죽이는데, 시벌 놈아. 키보드로 오러 블레이드 쓰는 새끼가 입만 살아 가지고.



치열한 갑론을박.

댓글을 다는 사람 중에는 강 건너 불구경하듯 바라보는 이들도 있었고, 이번 사태를 심각하게 받아들이는 이들도 있었다.

그렇게 종말론과 낙관론이 판을 치는 와중에도 새로운 소식은 끊임없이 업데이트되고 있었다.



(Best댓글) 안보리 오피셜, 한 시간 전 동서부 쪽 전선 뚫림. 다행히 파이 첸이 지원군으로 와서 피해 확산은 막았다고 함.

└ ㄷㄷ진짜네.

└ 동서부 전선이면 우헤이싱 있는 곳 아님?

└ 맞음. 중국 약쟁이 걔.

└ 근데 왜 뚫려. S급 헌터잖아.

└ 중국산 S급 헌터라 그럼.

└ 아…….

└ 파이 첸 없었으면 진짜 큰일 날 뻔했네. 파이 첸은 대격변 출신 웰메이드 헌터라 그런가.

└ 파이 첸은 부모님이 홍콩 국적이라 홍콩산임.

└ 윗 댓글 품질 관리 위원회에서 일하냐? ㅈㄴ 명쾌하네.

└ 그런 김에 한국산 헌터들 소식은 없냐.

└ 정 드래곤은 북부 전선 맡아서 우세 점하는 중이고, 시벌좌는 서부 전선에서 두세 번 승리했다고는 들었는데 그 후로 소식 없는 거 보니까 현상 유지 중인 듯.

└ 음…… 이정룡 실력이야 뭐 다 아니까 걱정은 안 하는데, 시벌좌는 무사하려나. 아직 A급 헌터잖아.

└ ??ㅋㅋㅋㅋ

└ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ 아직도 시벌좌를 A급 취급하는 순진한 놈이 있눜ㅋㅋㅋㅋㅋㅋㅋㅋ현직 A급 헌터로서 웃음밖에 안 나온다. 진태경 쟤는 그냥 괴물임ㅋㅋ



야야ㅇ야야야!! 지금 안ㄴ보리에서 서ㅂ 전선 현황 발표함!

└ 오, 시벌좌 소식 오랜만이다.

└ 엄청 다급하네. 서부 전선? 뭐라는데?

└ 뚫렸다는데?

└ 어?

└ 어?

└ 뭔 소리야. 설마 시벌좌 죽었음……?

└ 잠깐만. 이게 뭔 내용이지. 얘들아 나 다시 보고 온다. 메인에 떴으니까 너희도 직접 가서 보셈.

└ 아. 갑자기 개후달리네; 당장 들어가 본다.

└ ㄱㄱㄱㄱㄱ



신나게 댓글을 작성하던 네티즌들은 황급히 유엔 안보리 홈페이지에 접속했다.

일시적으로 과도한 접속자가 몰린 탓에 트래픽 초과로 기다리길 한참. 마침내 메인 화면에 뜬 발표 자료을 본 그들은, 자신의 눈과 귀를 의심할 수밖에 없었다.

“……저게 뭐야.”

몬스터 군단과의 대치 상황을 표시해 놓은 지도. 타원형의 전선을 형성한 그곳에는, 송곳처럼 움푹 파고든 서부 전선의 모습이 그려져 있었다.



……방금 확인하고 왔다. 진짜 뚫렸네.

└ 진태경 죽음? 피해 얼마나 됨?

└ 아니, 몬스터 쪽이 뚫렸다고.

└ ??

└ ???

└ 돌파 속도가 너무 빨라서 업데이트가 못 따라간 거였음.

└ ……말이 되냐?

└ 입 다물고 셔터 내려라. 오늘 주모 제삿날이다…….



* * *



곧 치열한 전투가 벌어질 전장은 혼잡했다. 끝없이 펼쳐진 황무지. 무수히 많은 몬스터가 시야에 들어온다.

어디선가 불어온 바람에 놈들이 뿜어내는 짙은 살기와 악취가 묻어 나왔다.

“시부럴 거. 많이도 모였네.”

내 중얼거림에 곁에 서 있던 최 팀장이 대답했다.

“죽여도, 죽여도 끝이 없군요.”

서부 전선에 투입되어 본격적인 전투가 시작된 지 나흘째. 항상 말끔하던 최 팀장의 모습은 더 이상 찾아볼 수 없다.

핏물과 먼지로 뒤덮인 그는 침착하면서도 깊게 가라앉은 눈동자로 날 바라보았다.

“언제 시작합니까?”

“글쎄요, 그건 우리 꼬마 사령관님 의견을 들어 봐야지. 안 그래?”

마지막 물음표는 최 팀장을 향한 것이 아니다.

줄곧 내 곁에서 떨어지지 않고 있던 스물한 살의 ‘꼬마 사령관’. 샤오 쉔이 대답했다.

「저는 진 선생님의 명령에 따르겠습니다!」

녀석의 반짝거리는 눈빛에 실소가 터져 나왔다.

“아직도 그놈의 선생님 타령은. 나한테는 먼저 말 놓으라고 하던 녀석이. 차라리 형님이라고 부르라니까.”

「저, 정말 그래도 됩니까?」

“너만 괜찮으면 된다고 했잖아. 그런데 부하들 보는 앞에서 이래도 되는 거냐? 너 이제 소장 진급 한다며?”

샤오 쉔이 번개 같은 속도로 고개를 저었다.

「아무 문제 없습니다! 혀, 혀, 형님!」

싸울 때는 무서울 정도로 침착한데, 평소에는 왜 이렇게 말을 더듬는지 모르겠다.

나는 뒤에 정렬한 공안무력부 소속의 헌터들을 바라봤다. 자그마치 천여 명에 달하는 숫자.

뜨겁게 달아오른 눈동자에는 강자를 바라보는 선망과 경이로움이 깃들어 있었다.

물론 그중에서도 독보적인 건 샤오 쉔이지만.

「명령을 내려 주십시오. 혀, 형님.」

“명령이라.”

나는 문득 하늘을 올려다봤다.

거대한 날개를 펼친 독수리가 우리의 머리 위를 맴돌고 있었다. 오늘도 느낌이 좋다.

“따라와. 지금껏 해 왔던 것처럼.”

「……!」

“지금 당장.”

나는 대답과 함께 발을 내디뎠다.

쩌저적.

발끝에 실린 만근의 힘에 지면이 거미줄처럼 갈라지며 움푹 꺼진다.

그리고 다음 순간.

쾅!

귀가 먹먹해지는 굉음과 함께, 나는 빛줄기가 되어 쏘아졌다.

‘염화일로(炎火一路).’

추위를 머금은 바람이 달아오르며 열풍으로 변한다.

땅, 바람, 풍경이 빠르게 스쳐 지나가던 그때, 등 뒤에서 거대한 함성이 터져 나왔다.

「돌격! 돌격하라!」

「중화의 후예여! 인민이여! 놈들을 모조리 쓸어버려라!」

「와아아아아!」

두두두두!

캬우우우우!

천지에 울려 퍼지는 인간의 함성과 몬스터의 괴성. 거대한 진동이 지축을 떨어 울린다.

그 혼란의 입구 속에서, 나는 손에 쥔 백염(白炎)을 힘차게 휘둘렀다.

콰아아아!

창날에서 솟아 나온 극양의 강기가, 막아서는 모든 것을 베었다.
```

## Final English reading copy

```markdown
# Chapter 389

It was a day when the cold snap had finally eased.

Students finally freed from the college entrance exam were busy either preparing to retake it or having fun, while office workers boarded public transportation with dark circles hanging beneath their eyes.

And in the midst of that peaceful, ordinary routine, a bombshell no one had expected dropped.



**[Breaking News—United Nations Security Council Makes Major Announcement]**



The roughly thirty-minute video began with Chairman Xiao Yang staring gravely into the camera.

“I stand before you as the ninth state chairman of the People’s Republic of China and a member of the United Nations Security Council to speak about the massive monster wave that has occurred in Sichuan Province.”

It was a bombshell that seized the attention of the entire world and sent all of Asia into upheaval.



* * *



One day passed. Then two. Then three. Even after four days, the situation had not calmed down.

There had been countless incidents and accidents since the Great Cataclysm, but the monster wave that had erupted in Sichuan Province was unprecedented in scale.

Chinese state chairman Xiao Yang declared official martial law, and peacekeeping forces were deployed to the front with the approval of the United Nations Security Council.

The entire world was watching.

The Asian countries bordering China were especially on edge.

South Korea was no exception. Even today, the Hunter Issues section of the country’s largest forum site was boiling like a cauldron over a charcoal brazier.



Here’s a summary of the situation so far.

Nobody here hasn’t watched the Security Council’s major announcement video, right? If there is, go outside and die. This is a genuine emergency. Even that northern supreme leader bastard has probably watched the whole thing on iTube and is lurking on this forum too.

Anyway, there were so many fucking vermin demanding a summary of something that could literally cost them their lives that I finally got fed up and wrote one.

**1. An unexplained massive wave occurred in Sichuan Province. The current estimated casualties are at least 300,000.**

Of course, that estimate is already a week old, and the current figure probably can’t even be compared to it. Realistically, I think it’s impossible to calculate the numbers.

**2. The Chinese government intervened, but the scale was completely insane.**

A monster army numbering at least tens of thousands has gathered around a creature called an Arch Lich.

The People’s Liberation Army and Air Force were thoroughly wrecked, and more than two thousand Hunters from the Public Security Armed Forces have gone missing. Communications were cut off because of magical interference, and satellite surveillance was neutralized, so they can’t even confirm whether anyone survived.

**3. The Chinese government secretly contacted several countries and hired several S-rank Hunters to suppress the situation as quickly as possible. The UN peacekeeping forces were deployed to the front two days ago, and they’re fighting desperately.**

The Security Council is updating the battle situation, so anyone interested can check here.

*(Link attached.)*

Everything below this is just my personal opinion, so you can skip it if you want.

**4. Anyone with a functioning brain knows this, but the current situation is not merely serious. Mainland China is basically hell on earth.**

They’re dragging every usable Hunter to the front, so the mana levels of other Gates, which are being neglected, are unstable too. Hyperinflation is happening everywhere.

The truly frightening part is this: if the front collapses and the monster army advances beyond Sichuan…

I’ll leave the rest to your imagination.

**5. So go to the supermarket and buy emergency rations before everyone gets completely fucked. Of course, I’m not telling you to hoard supplies and make an unfair profit.**

**6. It felt like a shame to end things here, so I’m adding some patriotic hype.**

Our Sibeol-jwa and Ares Guild’s Jung Dragon are both doing great work at the front. Keep stanning them as hard as you have been.

The end.



Within a few hours of being posted, the thread surpassed 100,000 views and caught fire with comments from netizens watching the situation closely.



**(Best Comment)** The situation really is as serious as the post says, but the author is laying it on a little thick lol. There are S-rank Hunters in the fight, plus a hundred thousand regular Hunters. What’s there to worry about? And is the military just sitting around?

└ Yeah, they’re fooling around in the maintenance units right now.

└ …………?

└ Didn’t you watch the news? All the Chinese military equipment broke down this time, exposing the largest military-procurement corruption scandal ever. They say it’s worth at least tens of trillions of won. Apparently more than one or two divisions are stuck.

└ Huh. This sounds really familiar.

└ Please replace the canteens already, you fucking assholes. I got discharged last year, so why does mine still taste like Normandy water? Every time I take a sip, I can’t tell whether my name is Kim Cheol Soo or James.

└ Corporal Kim. Tonight’s dinner is braised boneless pollock.

└ Not eating that shit.

└ Anyway, the military being stuck because of broken equipment is a problem, but they have manpower to spare, so they’ll be fine. Hunters are the only ones who can actually hurt the monsters anyway. There’s a bigger problem than that.

└ What?

└ The number of monsters has broken through 100,000.

└ ??

└ ?????

└ What do you mean, 100,000? Fuck off; don’t talk nonsense.

└ It’s not nonsense. It’s official from the UN Security Council. Follow the link in the post and check it yourself. It was posted five minutes ago.

└ Wow… fuck.

└ Judging by the reaction above, I guess it’s true. Holy shit.

└ No. I only reacted like that because it’s all in English and I have no idea what it says. I’m running it through Goggle Translate right now.

└ Is this guy insane?

└ But seriously, if the monster count has really passed 100,000, isn’t this a disaster? The largest monster wave so far didn’t even exceed a thousand, did it?

└ Obviously, the wave wasn’t this big in the beginning. The problem is that there’s an Arch Lich over there. Even the appearance of an ordinary Lich would be a major incident, but that thing is a top-tier named monster unknown even to the academic world. Realistically, most of the monsters currently fighting are undead revived by the Arch Lich.

└ Arch Lich: “Kaioken times one hundred.”

└ Then can’t we just kill the Arch Lich? If most of the monsters are undead, killing the controller should end it, right?

└ ???????

└ Who the hell is going to kill the Arch Lich, you bastard? You can only use Aura Blade on a keyboard, and your mouth’s still the only thing that works.

A fierce argument broke out.

Some commenters watched from a safe distance, as though observing a fire across a river, while others took the situation extremely seriously.

And even as doomsday theories and optimism battled for control, new updates continued to pour in.



**(Best Comment)** Security Council official: The front in the east-west sector was breached an hour ago. Fortunately, Pai Chen arrived as reinforcement and prevented the damage from spreading.

└ Damn, it’s true.

└ If it’s the east-west front, isn’t that where Wu Heixing is?

└ Yeah. That Chinese junkie guy.

└ But how did it break through? He’s an S-rank Hunter.

└ Because he’s a Chinese-made S-rank Hunter.

└ Ah…

└ It could’ve been a real disaster if Pai Chen hadn’t been there. Maybe it’s because Pai Chen is a well-made Hunter from the Great Cataclysm.

└ Pai Chen’s parents have Hong Kong citizenship, so she’s Hong Kong-made.

└ Does the commenter above work in quality control or something? That was fucking clear.

└ While you’re at it, does anyone have news about the Korean Hunters?

└ Jung Dragon is in charge of the northern front and gaining the upper hand. I heard Sibeol-jwa won two or three times on the western front, but there’s been no news since, so I guess they’re holding the line.

└ Hmm… Nobody needs to worry about Lee Jungryong’s skills, but is Sibeol-jwa safe? He’s still an A-rank Hunter.

└ ?? LOL

└ LMAOOOOOOOOOO

└ There’s still an innocent idiot who treats Sibeol-jwa like an A-rank Hunter? As a current A-rank Hunter, all I can do is laugh. That Jin Taekyung guy is just a monster lol



Hey heyheyhey!! The U—N Security Council just announced the w—estern front situation!

└ Oh, Sibeol-jwa news. Been a while.

└ That sounds incredibly urgent. The western front? What are they saying?

└ They say it broke through?

└ Huh?

└ Huh?

└ What the hell does that mean? Don’t tell me Sibeol-jwa died…?

└ Wait. What is this actually saying? Guys, I’m going back to check it again. It’s on the main page, so go look for yourselves.

└ Ah. I’m suddenly fucking terrified. I’m checking it right now.

└ Go go go go go



The netizens who had been enthusiastically writing comments hurriedly accessed the United Nations Security Council website.

Because too many visitors had flooded the site at once, they had to wait for quite some time after hitting the traffic limit. At last, when they saw the announcement that had appeared on the main page, they could do nothing but doubt their own eyes and ears.

“…What the hell is that?”

The map displayed the standoff with the monster army. The front line formed an oval, but the western front had been gouged inward like an awl.



…I just checked. It really broke through.

└ Is Jin Taekyung dead? How bad are the casualties?

└ No, the monsters’ line was breached.

└ ??

└ ???

└ The breakthrough happened so fast that the updates couldn’t keep up.

└ …Does that even make sense?

└ Shut up and pull down the shutters. Today is the tavern lady’s death anniversary…[^1]

[^1]: Korean internet slang calls for a tavern lady to pour celebratory drinks when national pride surges; the joke is that today’s celebration will work her to death.



* * *



The battlefield where a fierce battle was about to erupt was chaotic. An endless wasteland stretched out before us, and countless monsters filled my field of vision.

A wind that blew in from somewhere carried the thick killing intent and stench pouring off the creatures.

“Fuck. They really gathered a lot.”

Team Leader Choi, standing beside me, answered my mutter.

“No matter how many we kill, they never end.”

It was the fourth day since we had been deployed to the western front and the full-scale battle had begun. The Team Leader Choi who had always looked immaculate was nowhere to be found.

Covered in blood and dust, he looked at me with a calm, somber gaze.

“When do we begin?”

“Who knows? We should hear what our little commander thinks first. Right?”

That last question was not directed at Team Leader Choi.

The twenty-one-year-old “little commander” who had not left my side the entire time answered. It was Shao Shen.

“I will follow Teacher Jin’s orders!”

A snort of laughter escaped me at the sparkle in his eyes.

“You’re still going on about calling me Teacher. You were the one who first told me to drop the formal speech. I told you to call me hyung instead.”

“Is it… Is it really all right if I do that?”

“I told you it was fine as long as you were okay with it. But can you really do this in front of your men? I heard you’re getting promoted to major general now.”

Shao Shen shook his head at lightning speed.

“There’s no problem at all! H-hyung-nim!”

He was frighteningly calm when fighting, so I had no idea why he stammered so much in ordinary situations.

I looked at the Hunters from the Public Security Armed Forces lined up behind him. There were more than a thousand of them.

Their heated eyes held admiration and awe for the strong.

Of course, Shao Shen stood out even among them.

“Give us your orders. H-hyung-nim.”

“An order.”

I suddenly looked up at the sky.

A huge eagle with its wings spread wide circled above our heads. I had a good feeling about today, too.

“Follow me. Just like you’ve done until now.”

“……!”

“Right now.”

I stepped forward as I answered.

Crack.

The force of ten thousand geun packed into my toe made the ground split like a spiderweb and cave inward.

And then, in the next moment—

Boom!

Accompanied by a deafening roar that left my ears ringing, I shot forward as a streak of light.

*Flamefire Path.*

The wind carrying the cold heated up and transformed into a blast of hot air.

As the ground, wind, and scenery streaked past, a tremendous roar erupted behind me.

“Charge! Charge!”

“Descendants of Zhonghua! People! Sweep every last one of them away!”

“Waaaaaaah!”

Thud-thud-thud-thud!

Kyaaaauuuuu!

Human battle cries and monster shrieks rang across heaven and earth. The immense vibrations shook the very ground.

At the threshold of that chaos, I swung the White Flame in my hand with all my strength.

Whoooosh!

The Extreme Yang force that surged from the spearhead sliced through everything standing in its way.
```
