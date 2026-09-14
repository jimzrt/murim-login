<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0086.txt",
      "sha256": "06122d46467da177f5586bcdbf2c1c05099ba86cbb459b7474df63631dc2c8c7",
      "bytes": 13293
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "81d0f6ec215413c3736a52fc3511f22988b3b3130579fe5b406b88dd02db1c83",
      "bytes": 7872
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b6a11f0a546eb6ef6cdb0714045f8692ac4e160683858c989306708f8b4d8e68",
      "bytes": 8222
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "dc9e0cef79fc9570797777a10ca35419842acc39f1ad306b2aefd7d9328c24dc",
      "bytes": 1608
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1ca7a8224faf0cdc1914e2179bf2e9922360944aba454a27f766b1df68ff62f5",
      "bytes": 7127
    }
  ],
  "estimated_tokens": 13555
}
-->

# Durable State Update — Chapter 86

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 86. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 86. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 86,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 86,
    "continuity_sources": [86],
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
    "Taekyung successfully logged out after roughly twenty days in Murim; his watch showed 2:05:35 in the modern world, and ten modern-world days now correspond to one hour in Murim.",
    "Taekyung currently has fifteen years of internal energy, and circulating his qi slightly increases it; Sleep Mode normally keeps his sleep below three hours except when seriously injured.",
    "Team Leader Choi owns the café where Taekyung signed a contract providing a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.",
    "After ten days of Mukyung's training, Taekyung mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique, and the Training? Trial! Quest succeeded with a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured after the attack, and the unidentified assassin may be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training; Wikyung plans to summon every Shanxi sect on New Year's Day and may seek to become Alliance Leader.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months, and five-year-old Soyul does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout; Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect; Taekyung received the forced Yesterday's Enemy, Today's Ally Quest to deliver an invitation for New Year's Day.",
    "Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song. Butler Kim is Guild Master, Choi leads Team 1, and the other three are team members; Song Song is a C-rank healer.",
    "The Peace Guild's Guild house is Sooni's Super in Bucheon's Gate-dense district, on property purchased from the former owner's surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong is married with two children. Choi formerly served in Ares Guild with Song Song; Butler Kim is a retired mage and former Hunter who trained at Nonsan's 28th Regiment, 1st Battalion, as did Taekyung. Choi is Level 75, Kim Level 80, Song Song Level 64, and Im Hyeokjun Level 24.",
    "A Bucheon Terminal Guild raid against seven B-rank Minotaurs ended with the monsters defeated but two C-rank Hunters dead. Peace Guild then joined Sangdong Guild's party for its first official raid into The Minotaur's Labyrinth; Sangdong's team leader is Im Changsoo.",
    "Choi loaned Taekyung a Peak-grade Masterwork Black Drake Leather Set and a Peak-grade Masterwork Black Thorn Spear with a 90% chance to inflict Bleeding on hit.",
    "Sangdong Guild and Peace Guild entered The Minotaur's Labyrinth as a fifteen-person team with seven B-rank Hunters; Im Kkeokjeong was registered as an E-rank tank, and Taekyung received the restricted B-rank Gate Clear Quest. Taekyung is both a Hunter and a martial artist, and Choi has noticed that his behavior is inconsistent with an ordinary C-rank Hunter.",
    "Im Changsoo is the Sangdong Guild Master's son, behaves abusively toward his team, maintains a sponsorship relationship with the C-rank mage Hye-rin, and is Level 65. His team members depend on his financial support and obey his commands.",
    "Taekyung defeated all eight Minotaurs, received a Level Up, and established that Changsoo owes him 4 billion won and all byproducts. Changsoo agreed to pay and apologize after drawing his sword, and learned that Taekyung works as both a Hunter and a Murim martial artist.",
    "Changsoo planned to use Song Song as leverage, seize Taekyung's camera, and let the Minotaur Warrior exhaust Taekyung before humiliating him, but Taekyung killed the Level 70 boss monster with One Annihilation in a single blow.",
    "Taekyung completed the B-rank Gate Clear Quest, received another Level Up, and had the Quest Success Reward deposited into his Inventory."
  ],
  "continuity_sources": [
    85
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed, as does any connection between the attack and Song Sword Sect.",
    "It remains unresolved whether Hyuk Mujin will become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim's former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung's interrupted confession.",
    "Whether Im Changsoo fulfills his promised payment, surrenders the byproducts, and gives the demanded apology and damages remains unresolved."
  ],
  "safe_through": 85,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; render the current team dialogue's 형, 오빠, and 형님 as hyung, oppa, and hyungnim; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Render fist-and-kicking technique as 권각술, recognition as 인정, Falling Flow Sword as 낙류검, Twelve Gale Fists as 질풍십이권, Flame Divine Palm as 화염신장, and Tendon-Splitting and Bone-Twisting as 분근착골.",
    "Use Reformation Fist, Toughness, Heavenly Martial Physique, Jang Childeuk, Martial Artist Jang, benevolence/righteousness/propriety/wisdom, killed by a tiger, fifteen minutes, lifelong single, Let's eat noodles, Squad Leader, Third Young Master, Designer-Brand Junkie, Qi Sense, Peace Guild, Essence of the Himalayas, Sooni's Super, Song Song, Miss Song, Taurus, Ares Guild, Senior, Young Master, Guild Master, Minotaur, Bucheon Terminal Guild, The Minotaur's Labyrinth, and Shit Changsoo as established.",
    "Use Sangdong Guild, Hunter Association, Black Drake, Masterwork Black Drake Leather Set, Masterwork Black Thorn Spear, Bleeding, artifact, gear advantage, Hye-rin, Cheongdam-dong, Matador's Full-Body Armor, Matador's Shield, Taunt, Hallucination, Minotaur Warrior, Top-tier, tongue-pulling hell, big bills, baram wind/infidelity pun, Horndog, Hoengseong, Gangwon Province, Xyliton, Hongik Ingan, mind-reading technique, and One Annihilation as established terminology or translation choices."
  ],
  "version": 1
}
```

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
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |

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
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |

## Exact glossary matches

| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 명성               | **Fame**                       |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 대한민국 | **Korea** | Country reference. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 85
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

## Korean source

```text
＃86화



“아이고, 고생하셨습니다.”

담당 공무원이 허겁지겁 뛰쳐나와 우리를 맞이했다.

뭐, 정확히는 임창수를 맞이했다고 해야 옳겠지.

우리가 가져온 각종 부산물이며 마정석을 꼼꼼하게 확인한 그가 호들갑을 떤다.

“이야, 물량이 엄청나네요. 이 정도면 미로에 있는 미노타우로스들이 씨가 말랐겠어요.”

“…….”

창백한 안색의 임창수가 대답 없이 고개만 끄덕이니 담당 공무원이 눈치를 살폈다.

“팀장님, 혹시 편찮으신 곳이라도?”

언제부터 담당 공무원이 헌터 건강까지 챙겨 줬는지 모르겠군.

나는 괜한 말이 나오기 전에 임창수를 옆구리를 쿡 찔렀다.

“대답하셔야죠. 창. 수. 씨.”

“……아닙니다. 전 괜찮아요.”

“아, 그러시다면 다행이고요.”

이상한 분위기를 감지한 걸까? 담당 공무원이 미심쩍은 눈빛으로 나를 쳐다봤지만 딱 거기까지였다.

“부산물 처리는 어떻게 하시겠습니까? 아시는 대로 두 가지 방법이 있습니다만.”

담당 공무원의 말대로 부산물의 판매 방식은 두 가지로 나뉜다.

개인 판매와 위탁 판매. 전자의 경우는 말 그대로 해당 물품의 소유주인 개인이 알아서 거래를 하는 방식이고, 위탁 판매는 관리청, 즉 정부 기관에 맡겨 판매하는 거다.

‘각기 장단점이 있지.’

희소성이 있는 물건은 개인 판매가 이득이고, 그게 아니라면 정부 기관에 넘기는 게 속 편하다. 명품 경매와 시장 경매의 차이랄까?

“어떻게 할까요?”

임창수의 물음에 김 집사가 나섰다. 이번 게이트의 레이드에서는 한 번도 나선 적 없지만 그도 베테랑 헌터다. 오히려 이쪽에 대해선 이 중 누구보다도 더 빠삭할 것이다.

“관리청에 판매하겠습니다.”

소는 버릴 게 없다더니, 미노타우로스도 마찬가지였다.

가죽은 장비 제작에, 뼈는 푹 고아 보양식으로 쓰이며 뿔은 마니아들에게 수집품으로 인기가 있다.

“잘 생각하셨습니다.”

담당 공무원이 세상 기쁜 표정으로 부산물을 정산하기 시작했다. 사는 건 관리청인데 저 아저씨가 좋아하는 이유는 뻔하다.

‘떡고물 좀 떨어지나 보네.’

뭐, 담당 공무원이 얼마를 해 먹든 내 알 바 아니다.

오늘 내가 챙긴 떡고물이 훨씬 크니까.

툭툭.

“약속한 금액은?”

임창수가 바짝 굳은 얼굴로 대답했다.

“드, 드리겠습니다.”

“언제까지?”

“내일까지 보내 드리겠습니다.”

40억을 내일까지? 확실히 부잣집 아들이라 시원시원하다. 나는 활짝 웃으며 쪽지를 건넸다.

“어휴, 그럼 나야 좋지. 여기 내 계좌 번호. 가보처럼 간직하고 있다가 내일 보내 줘. 나중에 잃어버렸다고 하면 재미없어요. 알죠?”

“……넵.”

이 정도면 됐겠지? 나는 임창수의 등을 툭 치는 걸로 작별 인사를 대신했다.

비틀거리는 걸음으로 멀어지는 녀석의 뒷모습을 흐뭇하게 지켜보고 있던 내게 임꺽정이 물었다.

“저놈이 약속한 돈을 줄까?”

“안 주면요?”

“그 뭐냐. 좀 거시기 하잖아. 상동 길드면 근방에서 힘깨나 쓰는 중견 길드인데. 저놈이 배 째라 식으로 나오면…….”

“에이, 증거 영상도 있는데 설마.”

“증거야 없애면 되는 거고. 뭣보다 내가 좀 들은 게 있어서 그래.”

“그게 뭔데요?”

이렇게까지 말하니까 살짝 신경이 쓰이기 시작한다.

잠시 눈치를 살피며 주위를 두리번거린 임꺽정이 작은 목소리로 속삭였다.

“상동 길드장. 누군지는 대충 알지?”

“네. 이름은 오늘 처음 들어 봤지만.”

임춘수. 왠지 모르게 술배 불룩하게 나온 중년 아저씨가 연상되는 이름이지만 상상과 현실은 정반대다.

“대격변 때 혁혁한 전공을 세웠던 A급 헌터잖아요. 사람들이 뭐라고 부르더라? 프, 프. 갑자기 생각이 안 나네.”

“프로즌(Frozen).”

“아, 맞다. 프로즌. 빙결 전문 마법사.”

유명한 헌터들의 경우 그에 맞는 이명(異名)이 붙는다.

임춘수의 경우도 그랬다. A급 헌터인 그는 대격변에서 큰 활약을 보여 준 마법사였고, 그중에서도 특히 빙결 관련 마법에 능해서 프로즌이라는 이명이 붙었다.

“그 양반이 빙결 계통으로는 국내 다섯 손가락 안에 들지. 그 명성을 바탕으로 지금의 상동 길드를 키워 낸 거고.”

처절했던 대격변이 종막을 고하자 1세대 헌터들은 선택의 기로에 섰다. 은퇴를 할 것인가, 현역으로 남을 것인가. 임춘수는 후자를 선택했고 상동 길드를 세웠다.

“대단하네요. 아들은 별거 없던데.”

아무리 A급 헌터라도 맨주먹 하나로 대격변에서 살아남아 부와 명예 모두를 얻은 경우는 흔치 않다. 임춘수의 현재는 많은 헌터들이 꿈꾸는 미래다.

“대단? 확실히 대단하지. 핏줄이라는 게.”

임꺽정이 멀어져 가는 임창수의 뒷모습을 턱짓했다.

“저 녀석이 누구 피를 물려받았는지 잊지 마라.”

“그게 무슨…….”

“자랑은 아니지만 내가 이 바닥 생활 시작한 지 20년이 넘었어. 내가 생초짜이던 시절에 상동 길드가 세워졌지.”

“그런데요?”

“지금도 그렇지만 당시 부천은 길드들끼리 경쟁이 치열했거든. 도저히 신생 길드가 끼어들 틈이 없었어.”

“임춘수는 그걸 뚫었다?”

“그렇지. 그래서 무서운 사람인 거고.”

“음.”

이게 그렇게 연결이 되나?

길드 간 경쟁 심리야 하루 이틀 일이 아니고 능력 있는 쪽이 살아남는 건 실력 위주의 사회에선 당연한 일이다.

“그 사람 정도면 헌터로서의 능력도 출중하고 명성도 있었잖아요. 인맥도 빵빵했을 거고.”

“다른 길드장들은 아니었을 것 같냐?”

“네?”

“임춘수에 비해 명성은 조금 부족했을지 몰라도 하나같이 다 전쟁 영웅 출신들이었어. 상동 길드보다 몇 년이나 앞서 시장을 개척하고 상당수의 게이트를 점유하고 있었지.”

임꺽정이 낮은 목소리로 말을 이었다.

“아직 체계가 완벽히 잡히지 않아서 온갖 불법이 횡행할 때였다. 지금 상동 길드가 존재할 수 있는 건 임춘수가 경쟁자들을 모두 박살 냈기 때문이야. 결코 호락호락한 사람이 아니라는 거지.”

문득 뇌리를 스치는 생각이 있었다.

임춘수가 오늘 있었던 일을 알게 된다면? 하나뿐인 아들이 개망신을 당했다는 말에 어떤 반응을 보일까?

‘일이 좀 꼬일 수도 있겠는데.’

대한민국 하면 빼놓을 수 없는 것이 학연, 지연, 혈연이다.

20년간 한자리를 굳건히 자리를 지킨 상동 길드가 지역 유지라면 우리 길드는 신생아나 다름없는 수준.

상동 길드가 작정하고 덤비면 출생 신고서부터 찢어질 거다.

“혹시 상동 길드장, 성격 좋아요?”

“나야 모르지. 소문으로만 대충 들었어.”

“그것만이라도 알려 줘요.”

잠시 고민하던 임꺽정이 대답했다.

“오늘 임창수를 보니까 옛말이 하나 떠오르더라. 호부견자(虎父犬子).”

“훌륭한 아버지에 못난 아들이라면 어쨌든 좋은 뜻이잖아요. 말은 통하는 사람인가?”

“아니, 한자 그대로 해석해 봐.”

“……호랑이 아버지에 개 아들?”

“임창수 성격이 개새끼면 임춘수는 호랑이야. 성격이 아주 지랄 맞대.”

“…….”

“나이 먹고 성격 죽었다는 얘기도 있는데, 사람 성격이 그렇게 쉽게 바뀔까 싶다.”

이런 시발.

들으면 들을수록 왠지 등골이 서늘한 게, 꼭 무슨 일이 하나 터질 것 같은 느낌이다.

‘아씨, 내기하지 말 걸 그랬나.’

수십억을 받을 생각에 한껏 들뜬 것도 잠시. 이제는 큰일 보고 뒤 안 닦은 것처럼 찝찝하다.

나야 둘째치고 다른 길드원들이 피해를 입는 건 절대 사양인데.

“태경아, 너무 신경 쓰지 마라. 나도 혹시나 해서 말해 본 거니까.”

“이거 사고 친 거 아니겠죠?”

“괜찮아. 최 팀장도 재미있다고 내기 거들었잖아.”

“어, 맞네?”

“그렇지. 그리고 임창수 저놈 하는 짓 봐라. 내가 아버지였으면 반쯤 죽여 놨을걸. 쪽팔려서 어디에 말도 못 해.”

확실히 일리가 있군. 뭐 별일이야 있겠어?

그 얘길 들으니 한결 마음이 가벼워진다. 저절로 웃음이 나올 정도다.

“고마워요. 꺽정 아저씨, 아니 형님.”

“그럼 갑부 된 기념으로 소고기 사. 아니지, 나 말고 송 양이랑 먹어야지.”

“……아.”

가슴에 대못을 박는구나.

사람 두 번 죽이는 임꺽정의 말에 나는 눈물을 삼켰다.



* * *



“무슨 일로 왔나?”

목소리의 주인은 이색적인 외모의 사내였다.

오십 줄에 접어든 나이였으나 피부는 팽팽했고 철사처럼 뻗친 머리카락은 검었다. 부리부리한 눈매는 보는 것만으로도 오금을 저리게 했다.

‘무슨 놈의 눈빛이…….’

K은행의 지점장에게도 그건 예외는 아니었다. 이미 수차례 만난 적 있지만 자신은 일반인이었고 상대는 A급 헌터, 그것도 대격변을 온몸으로 겪은 산증인이 아닌가.

저절로 혀가 꼬이고 식은땀이 흘렀다.

“그게…….”

“아까운 시간 뺏으러 온 거면 그만 돌아가고. 아니면 이 자리에서 당장 얘기하게.”

내용은 날이 섰지만 말투는 제법 온화하다.

나이 먹고 성격 죽이려고 노력한다는 소문은 들었는데 아예 헛수고는 아닌 모양이었다.

‘에이, 시발.’

지점장은 눈을 딱 감고 질렀다.

“죄송합니다, 길드장님. 아드님 일로 찾아뵈었습니다.”

아드님. 그 세 글자에 상동 길드장 임춘수의 눈썹이 꿈틀거렸다.

“창수? 그 녀석이 왜?”

“일전에 아드님께서 은행 관련 업무를 이용하게 되면 꼭 알려 달라고 하셔서…….”

임춘수가 감 잡았다는 듯이 고개를 끄덕였다.

“이번엔 뭔가? 내 인감이라도 훔쳤나? 아니면 담보 대출?”

“상당한 금액을 한 번에 이체하셨습니다.”

“또 계집질이겠지. 뻔해. 액수가 어떻게 되나?”

“두 개의 계좌에 각기 40억씩. 합해서 80억입니다.”

“얼마?”

“80억…… 헙.”

지점장은 황급히 숨을 삼켰다. 임춘수의 등 뒤에 있는 유리창이 빠르게 얼어붙는 광경을 목격했기 때문이었다.

파스스.

밖은 늦여름인데 사무실을 지배한 것은 추위와 냉기다.

오들오들 떨고 있는 지점장에게 그가 손짓했다.

“더 할 말은?”

“과, 관련 자료를 가져왔습니다.”

지점장이 떨리는 손으로 책상 위에 서류 뭉치를 내려놨다.

“잘했어. 이만 나가 보게.”

“다, 다음에 뵙겠습니다.”

지점장이 도망치듯 방 안을 빠져나간 뒤 임춘수는 수화기를 들었다. 냉기 저항 기능이 있는 전화기는 아무 문제 없이 빠르게 신호를 발신했다.

뚜, 뚜, 달칵.

- 네. 길드장님. 1팀장 전화 받았습니다.

“그 자식 당장 잡아 와.”

- ……임창수 팀장 말씀이십니까?

“팀장은 무슨. 오늘부터 해고야. 그 새끼 당장 잡아 와!”

쾅! 수화기의 수명은 거기까지였다. 수백 조각으로 나뉜 얼음 파편이 책상 위를 덮었다.

“이런 한심한, 내 그리 일렀는데도…….”

서늘한 눈으로 난장판이 된 사무실을 노려보던 임춘수의 시선이 한곳에 멎었다. K은행의 지점장이 놓고 간 서류 뭉치.

저 안에 80억의 행방이 들어 있을 게 분명했다.

‘멍청한 놈. 이번에는 어느 년한테 홀랑 넘어간 거냐?’

한 장, 한 장 넘겨 가며 읽기를 십여 분.

임춘수가 마지막 장을 덮었을 때, 누군가 질질 끌려오는 소리와 함께 문이 활짝 열렸다.

“임창수 팀장. 여기 데려왔습니다.”

푸근한 인상의 중년인. 그리고 중년에게 꽉 붙잡힌 한 청년.

“아, 아버지!”

“내 자랑스러운 아들 왔구나.”

아들의 등장에 아버지가 손을 내밀었다.

물론 결코 용서의 의미는 아니었다.

파츠츠츠.

임춘수의 손아귀에서 냉기가 솟구친다. 기체에서 액체, 액체에서 고체로 변한 그것은 강철만큼 단단한 얼음 몽둥이로 변화를 끝마쳤다.

“물어볼 게 많지만 우선 맞자.”

“아버지!”

“닥쳐, 이 새끼야!”

임창수를 데려온 중년인, 상동 길드의 1팀장은 조용히 문을 닫았다. 앞으로 반나절 동안 이곳은 출입 금지다.
```

## Final English reading copy

```markdown
# Chapter 86

“Oh, thank you for your hard work.”

The government official in charge came rushing out to greet us.

Well, more accurately, he came to greet Im Changsoo.

After meticulously checking all the byproducts and Magic Gems we had brought, he made a fuss.

“Wow, that’s an incredible amount. There can’t be many Minotaurs left in the labyrinth after this.”

“…”

Im Changsoo’s face was pale. He only nodded without answering, making the official glance around uneasily.

“Team Leader, are you feeling unwell?”

Since when did government officials start worrying about Hunters’ health?

Before he could say anything unnecessary, I jabbed Im Changsoo in the ribs.

“You have to answer him. Chang. Soo.”

“Um… No, I’m fine.”

“Ah, that’s a relief, then.”

Maybe he had sensed the strange atmosphere. The official looked at me suspiciously, but that was as far as it went.

“How would you like to handle the byproducts? As you know, there are two methods.”

As the official explained, there were two ways to sell byproducts.

Personal sales and consignment sales. With the former, the individual owner of the goods handled the transaction personally. With the latter, the goods were entrusted to the Administration, meaning a government agency, for sale.

*Each method has its pros and cons.*

Rare items sold better privately. For everything else, handing it over to a government agency was less of a hassle. It was like the difference between a luxury auction and a market auction.

“What should we do?”

At Im Changsoo’s question, Butler Kim stepped forward. He hadn’t once taken the lead during this Gate raid, but he was still a veteran Hunter. When it came to this sort of thing, he probably knew more than anyone else here.

“We’ll sell them to the Administration.”

They said there was nothing to waste from a cow. The same went for Minotaurs.

Their hides were used to make Equipment, their bones were boiled down into restorative food, and their horns were popular collector’s items among enthusiasts.

“You made the right choice.”

The government official began calculating the byproducts with an expression of pure delight. The Administration was the one buying them, so the reason he was happy was obvious.

*He must be getting a little something off the top.*

Still, whatever the official skimmed off wasn’t my concern.

The cut I was getting today was much bigger.

Tap, tap.

“What about the agreed-upon amount?”

Im Changsoo answered with a rigid expression.

“I-I’ll pay it.”

“By when?”

“I’ll send it by tomorrow.”

Four billion won by tomorrow? The son of a rich family certainly knew how to be decisive. I smiled broadly and handed him a slip of paper.

“Well, that works for me. Here’s my account number. Keep it safe as if it were an heirloom, then send the money tomorrow. It won’t be funny if you say you lost it later. Got it?”

“…Yes, sir.”

That should be enough, right? I said goodbye by giving Im Changsoo a light pat on the back.

As I watched with satisfaction as he staggered away, Im Kkeokjeong asked me,

“Do you think that punk will actually pay?”

“What happens if he doesn’t?”

“You know… it could get a little awkward. Sangdong Guild is a mid-tier Guild with some serious influence around here. If he decides to brazen it out and refuses to pay…”

“Come on, we have video evidence. Surely he wouldn’t.”

“Evidence can be destroyed. More importantly, I’ve heard a few things.”

“Like what?”

Now that he had put it that way, I was starting to get a little worried.

Kkeokjeong glanced around, checking everyone’s reactions, then leaned in and whispered,

“You know who the Sangdong Guild Master is, right?”

“Yes. I heard his name for the first time today, though.”

Im Chunsoo. For some reason, the name brought to mind a middle-aged man with a bulging drinker’s belly, but reality was the exact opposite.

“He’s an A-rank Hunter who made an impressive name for himself during the Great Cataclysm. What do people call him again? Fro… Fro… It’s suddenly slipping my mind.”

“Frozen.”

“Ah, right. Frozen. A mage specializing in ice magic.”

Famous Hunters were often given nicknames to match their abilities.

The same was true of Im Chunsoo. An A-rank Hunter, he had made a name for himself as a mage during the Great Cataclysm. He was particularly skilled with ice-related magic, which had earned him the nickname Frozen.

“When it comes to ice magic, that man is one of the top five in Korea. He used that Fame to build Sangdong Guild into what it is today.”

When the brutal Great Cataclysm finally came to an end, the first-generation Hunters faced a choice.

Retire, or remain active.

Im Chunsoo chose the latter and founded Sangdong Guild.

“That’s impressive. His son doesn’t seem like much.”

Even among A-rank Hunters, it was rare for someone to survive the Great Cataclysm with nothing but their bare fists and gain both wealth and fame. Im Chunsoo’s present was the future many Hunters dreamed of.

“Impressive? It certainly is—the power of bloodlines, that is.”

Kkeokjeong jerked his chin toward Im Changsoo’s retreating back.

“Don’t forget whose blood that punk inherited.”

“What does that…”

“I’m not bragging, but I’ve been in this business for over twenty years. Sangdong Guild was founded when I was still a complete rookie.”

“And?”

“Bucheon was just as fiercely competitive between Guilds back then as it is now. There was no room for a new Guild to squeeze in.”

“But Im Chunsoo broke through anyway?”

“That’s right. That’s why he’s a frightening man.”

“Hmm.”

Did that really mean so much?

Competition between Guilds was nothing new, and in a merit-based society, it was only natural for the capable to survive.

“A man like him would have had excellent abilities as a Hunter and plenty of Fame. He must have had powerful connections, too.”

“Do you think the other Guild Masters didn’t?”

“What?”

“They might have had slightly less Fame than Im Chunsoo, but every one of them had been a war hero. They had entered the market several years before Sangdong Guild and occupied a substantial number of Gates.”

Kkeokjeong continued in a low voice.

“It was a time when all kinds of illegal activity ran rampant because the system hadn’t been fully established yet. The only reason Sangdong Guild exists today is that Im Chunsoo crushed every one of his competitors. He’s no pushover.”

A thought suddenly flashed through my mind.

What would happen if Im Chunsoo found out about what had happened today? How would he react to hearing that his only son had been utterly humiliated?

*This could get complicated.*

When you talked about Korea, you couldn’t leave out connections through school, region, and blood.

Sangdong Guild had held its ground for twenty years. If it was a local power, our Guild was practically a newborn.

If Sangdong Guild came at us in earnest, they’d tear up our birth certificate before we even got started.

“Is the Sangdong Guild Master a nice person, at least?”

“I wouldn’t know. I’ve only heard rumors.”

“Tell me what you’ve heard.”

After thinking for a moment, Kkeokjeong answered,

“Seeing Im Changsoo today reminded me of an old saying. A tiger father and a dog son.”

“A great father and a worthless son? That’s still a compliment, isn’t it? Is he the kind of person you can reason with?”

“No. Try interpreting it literally.”

“…A tiger for a father and a dog for a son?”

“If Changsoo’s personality is that of a son of a bitch, then Im Chunsoo is a tiger. I hear his temper is absolutely fucking terrible.”

“…”

“I’ve also heard that he mellowed out with age, but can a person’s temper really change that easily?”

*For fuck’s sake.*

The more I heard, the colder my spine felt. I had the distinct feeling that something was about to go horribly wrong.

*Damn it. I shouldn’t have made that bet.*

My excitement at the thought of receiving several billion won had lasted only a moment. Now I felt uneasy, like I had taken a huge dump and forgotten to wipe.

I didn’t care what happened to me, but I absolutely refused to let the other Guild members get hurt.

“Taekyung, don’t worry about it too much. I only brought it up just in case.”

“I didn’t just cause trouble, did I?”

“It’ll be fine. Team Leader Choi thought it would be fun and joined the bet, too.”

“Oh, right.”

“Exactly. And look at the way Im Changsoo acted. If I were his father, I would’ve beaten him half to death. He’d be too embarrassed to tell anyone about it.”

He had a point. What could possibly happen?

Hearing that made me feel considerably lighter. I even found myself smiling.

“Thanks, Kkeokjeong ajusshi. No, hyungnim.”

“Then buy us some beef to celebrate becoming a rich man. Wait, no. You should eat it with Miss Song, not me.”

“…Ah.”

He was driving a nail straight through my heart.

As Im Kkeokjeong killed me with words for the second time, I swallowed my tears.

* * *

“What brings you here?”

The speaker was a man with a distinctive appearance.

He was nearing fifty, but his skin was taut and his wiry, spiky hair was black. His large, piercing eyes were enough to make anyone’s knees go weak.

*What the hell is with that look in his eyes…*

The manager of a K Bank branch was no exception. He had already met the man several times, but he was an ordinary person, while the other man was an A-rank Hunter—a living witness who had endured the Great Cataclysm with his entire body.

His tongue tied itself in knots, and cold sweat trickled down his back.

“Well…”

“If you came to waste my valuable time, go back. Otherwise, speak now.”

The words were sharp, but his tone was fairly gentle.

The manager had heard the rumor that Im Chunsoo was trying to mellow his temper with age. Apparently, it hadn’t been a complete waste of effort.

*Damn it.*

The branch manager steeled himself and blurted out,

“I’m sorry, Guild Master. I’ve come regarding your son.”

At the mention of his son, Sangdong Guild Master Im Chunsoo’s eyebrow twitched.

“Changsoo? What about him?”

“Some time ago, you asked me to let you know whenever your son used any of the bank’s services…”

Im Chunsoo nodded as if he understood.

“What is it this time? Did he steal my seal? Or take out a loan against collateral?”

“He transferred a considerable amount of money all at once.”

“He must be fooling around with women again. Obviously. How much?”

“Four billion won to each of two accounts. Eight billion won in total.”

“How much?”

“Eight billion… Hup.”

The branch manager hurriedly swallowed his breath. He had just watched the window behind Im Chunsoo rapidly freeze over.

Hiss.

It was late summer outside, but the office was suddenly ruled by cold and frost.

Im Chunsoo gestured at the trembling branch manager.

“Anything else?”

“I-I brought the relevant documents.”

With shaking hands, the branch manager placed a stack of papers on the desk.

“Good. You may leave.”

“I-I’ll see you next time.”

After the branch manager fled the room, Im Chunsoo picked up the receiver. The phone had a cold-resistance function, so it transmitted the signal without any problems.

Beep, beep. Click.

—Yes, Guild Master. Team One’s Leader speaking.

“Bring that bastard here immediately.”

—…Do you mean Team Leader Im Changsoo?

“Team Leader, my ass. He’s fired as of today. Bring that bastard here now!”

Bang!

The receiver’s life ended there. Ice shattered into hundreds of pieces and covered the desk.

“What a pathetic fool. Even after I warned him…”

Im Chunsoo glared coldly at the wrecked office, then his gaze stopped on one spot: the stack of papers left behind by the K Bank branch manager.

There was no doubt that the documents contained the whereabouts of eight billion won.

*You stupid bastard. Which woman did you fall for this time?*

He read through the papers, turning them one page at a time, for more than ten minutes.

When Im Chunsoo closed the final page, the door flew open with the sound of someone being dragged along.

“Team Leader Im Changsoo. I brought him here.”

An affable-looking middle-aged man stood there. In his firm grip was a young man.

“F-Father!”

“My proud son has arrived.”

At his son’s appearance, the father extended a hand.

Of course, it was not meant as a gesture of forgiveness.

Crackle, crackle, crackle.

Cold surged from Im Chunsoo’s grasp. It changed from gas to liquid, then from liquid to solid, completing its transformation into an ice club as hard as steel.

“I have a lot to ask you, but first, you’re getting hit.”

“Father!”

“Shut up, you little shit!”

The middle-aged man who had brought Im Changsoo there—the Team Leader of Sangdong Guild’s Team One—quietly closed the door.

For the next half a day, no one was allowed to enter.
```
