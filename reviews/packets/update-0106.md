<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0106.txt",
      "sha256": "becf6afa54fc27c23a68fd09b99c66d949a09a5542b8904a7590c09b00acd59c",
      "bytes": 14742
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "91532b8b6bbd83cf5ede9346e62c75e3fabef39bae606b278293962369ead46e",
      "bytes": 4359
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bf8acbe4b21a37d67ce4c93a4f9c9d2bfd024d0afd06d2df7afaa87e0881a2a2",
      "bytes": 13960
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ceaa19d1c191642371a803f8c122efe078af75530e361f8700881aa5ccd99330",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "eb975423e1badc2ead87a8f1493d62e3c394784f4a28b16326657c9accf086ef",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d6dc7973ce67cf69c3c70a753765c94db6951e6b890ba30a0085e4f07b0d458d",
      "bytes": 24117
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "77d6d0386b42c24bcec305b7f4cf658e0dd24b2c94f207cd8c60594381d938d0",
      "bytes": 8154
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "00e0690dead9e78b66fbbc717f43809151bc18e6e8dd93b451289bd7bb9cfd6b",
      "bytes": 2803
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "1c997c68e63085990d4efdf27c96924072d7f249f79e7bfa850c3c2894bb4b5b",
      "bytes": 2201
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "17bb03c455319c716952598f9355f806722a45e0b8a0d0c0469d20b2690042b8",
      "bytes": 14172
    }
  ],
  "estimated_tokens": 18342
}
-->

# Durable State Update — Chapter 106

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 106. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 106. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 106,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 106,
    "continuity_sources": [106],
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
    "Sangdong Guild's Security Team was assigned to surveil Jin Taekyung; the property being used as its surveillance base remains unidentified.",
    "Choi Byungil led the failed operation against Taekyung and was defeated with the other field Hunters; the Security Team faces written discipline, a pay cut, and possible dismissal.",
    "Kim Junsu is the Security Team's sole Familiar mage, and Hong Woojin is an outside B-rank Familiar mage hired by Team Leader 1.",
    "Seong Jinho is Taekyung's thirty-year-old civilian goshiwon manager and sworn-brother-like friend in Bucheon.",
    "Im Chunsoo is a Level 75 A-rank ice mage and Guild Master of Sangdong Guild.",
    "Kim Hwajong is a Level 80 mage and former Hunter Training Center instructor; he trained Im Chunsoo, who was a Class 25 trainee assigned to the 28th Regiment, First Battalion, Second Company.",
    "The reason Kim Hwajong arrived at the confrontation remains unknown, as does why he now works as a butler.",
    "Team Leader 1 assesses Taekyung as a top-tier B-rank or A-rank Hunter.",
    "Taekyung owns a two-story detached house in Goyang intended as his family's home and will live there alone until Hayeon finishes her college entrance exam.",
    "Logout is active, so Taekyung no longer needs the capsule to travel between the modern world and Murim.",
    "Seong Jinho unexpectedly emerged from Taekyung's capsule inside the new house after Taekyung logged into Murim; how and why he entered remains unknown.",
    "Taekyung, Mukyung, and Hyuk Mujin have reached Honju and are staying at the Phoenix Inn's private residence.",
    "Mukyung is a Peak master and uses a superficially learned heat-yang technique to warm Hyuk Mujin.",
    "Taekyung must deliver the Jin Family of Taiyuan's Lunar New Year invitation to the weakened Mount Heng Sword Sect, now led by Lee Seowol, his uncomfortable former accuser.",
    "Hyuk Mujin is a First Rate martial artist from a tenant-farmer family, Captain of the Jin Family's Gatekeepers, deputy squad leader of White Tiger Hall's reconnaissance squad, and a candidate to become the next Master of the Gatekeeper Pavilion.",
    "Jin Wikyung gave Mujin fifty silver nyang for the journey and ordered the travelers to use good lodging and meals because they had no attendants.",
    "Mukyung considers enduring hunger a form of training, while Taekyung's appetite causes Mujin severe financial anxiety.",
    "The Phoenix Inn attackers were an organized group bearing running-horse tattoos; Wolhwa said Lee Cheonbaek had hired mounted-bandit groups from the northern plateau.",
    "Wolhwa is the Phoenix Inn's proprietress, a courtesan, and the Lower District Sect's Shanxi Branch Leader; she offered to accompany Taekyung to the Mount Heng Sword Sect."
  ],
  "continuity_sources": [
    105
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong, despite his former instructor status and exceptional ability, now works as a butler remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol will react to the invitation remains unknown.",
    "Whether Taekyung will accept Wolhwa's proposal to accompany him remains unknown."
  ],
  "safe_through": 105,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술 and keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you; render 김화종's 춘수 and 교관님 as Chunsoo and Instructor.",
    "Render 1번 훈련생 as Trainee Number One and 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year.",
    "Render 봉황객잔 and 계용옥미갱/계용옥미앵 as Phoenix Inn and chicken-and-corn soup.",
    "Render 곡도 as curved saber.",
    "Render 마적 and 마적단 as mounted bandits and mounted-bandit groups.",
    "Preserve Wolhwa's playful Young Master forms when addressing Taekyung."
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
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |

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
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 항산     | **Mount Heng**         |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 105
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 104
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 104
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 105
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 89
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 105
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, and quietly amused; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃106화



“같이 가요. 항산검문.”

“네?”

“진 공자가 들은 그대로예요. 나도 항산검문에 볼일이 있거든.”

“무슨 일로요?”

“그건 말 못 할 것 같은데? 나도 공과 사가 뚜렷한 편이라서.”

되로 주고 말로 받았군.

방금 내 입으로 한 말이 고스란히 돌아온다. 머쓱해하는 나를 보는 월화의 미소가 짙어졌다.

“장난이에요. 마침 항산검문 쪽에 받을 게 있거든요. 정확히는 태원진가에서 받기로 한 거지만.”

“무슨…… 아.”

문득 떠오르는 기억이 있다. 항산검문과의 전쟁이 한창 진행되고 있을 무렵, 태원진가와 하오문이 맺었던 밀약.

‘정보를 제공하는 대신 항산검문이 소유한 부지 등에 대한 소유권을 받기로 약속했던가?’

하오문은, 아니 월화는 약속을 지켰다. 개전 초기 항산검문의 선봉대를 궤멸시킬 수 있었던 것도 그녀의 도움이 있었기 때문이다.

태원진가는 그 후에도 하오문에게 여러 도움을 받았고 마침내 전쟁에서 승리했지만, 문제는 그 후였다.

“진 공자도 알다시피 우리 입장이 좀 묘하게 됐어요. 전쟁에선 이겼는데 전리품에 손을 못 대고 있는 상황이라.”

약육강식. 강자가 약자를 집어삼키는 건 무림의 법칙이다.

그러나 대장로의 등장이 모든 걸 망쳤다. 태원진가와 항산검문이 그의 농간에 놀아났다는 사실이 밝혀진 순간부터 전리품을 취할 명분이 희미해진 거다.

‘그래서 합병을 진행하는 거고.’

지금은 검을 거두고 붓으로 대화를 나눠야 할 때다. 세상 사람들이 욕하지 않는 범위 안에서 조용히, 원만하게 흡수하는 것이 진위경이 그리는 그림이다.

월화는 그 전에 보상을 받기를 원하는 거고.

“항산검문 측이 우리의 제안을 받아들인다면 그때 보상을 요구해도 될 텐데요.”

“그건 태원진가가 산서성의 맹주(盟主)가 아닌 패자(霸者)일 때나 가능한 이야기예요. 지금 상황에서 섣불리 뺏으려 하다가는 다른 중소 문파들도 발을 빼겠죠. 더군다나…….”

순간 나를 의미심장한 눈빛으로 바라본 그녀가 고개를 저었다.

도대체 뭐지?

“더군다나, 뭐요?”

“아니에요. 뭐, 아무튼 소가주님께도 제안을 받긴 했어요.”

월화가 곰방대를 뻐끔거리며 말을 이었다.

“약속했던 것에 상응하는 재물, 혹은 태원진가가 관리하는 구역을 양도해 주시겠다고 하더군요.”

그 정도면 괜찮은 거 아닌가 싶지만 개인이 아닌, 한 단체를 이끄는 수장의 입장에서 생각해 보면 다르다.

‘활동 영역을 확대하고 싶은 거겠지.’

월화의 본질은 기녀도, 객잔의 주인도 아닌 정보 상인.

이번 기회에 항산검문의 차단으로 비교적 약세였던 산서성 북부까지 하오문의 영향력을 넓히고 싶어 하는 게 분명했다.

‘진위경이야 당연히 태원진가가 산서성 전역을 아울렀으면 하는 마음일 거고.’

이미 오래전부터 산서성 중남부에 막대한 영향력을 행사해 왔던 태원진가다. 알짜배기 구역을 몇 개 넘겨준다고 해서 지금까지 쌓아 올린 영향력이 줄어들지는 않는다.

‘이거 딱 그거네. 재개발 구역.’

북부를 꽉 잡고 외부 세력의 유입을 막던 항산검문이 무너지고 있다. 그린벨트가 해제되고 재개발 구역이 되니 진위경과 월화 간의 밀고 당기기가 시작된 거다.

‘둘 다 장난 아니네.’

어제의 동맹이 오늘의 경쟁자가 됐다.

사람은 보이는 게 전부가 아니라는 사실을 오늘 다시 한번 느낀다.

“그래서 우리 귀여운 신임 문주님도 뵙고, 빚 독촉도 할 겸 항산검문까지 동행하려고 하는데…… 어때요?”

더 생각할 것도 없이 대답했다.

“거절하겠습니다.”

“와, 너무 단호한 거 아니에요? 거래 조건도 듣기 전에 칼같이 잘라 버리네.”

“아우가 돼서 형님 앞길에 똥물 뿌릴 순 없죠.”

피 한 방울 안 섞인 형제지만 이미 마음 한구석에서는 그의 존재를, 이 무림을 받아들인 지 오래다.

“흐음.”

나를 지그시 바라보던 월화가 곰방대를 탁 내려놨다.

“그렇게 해요, 그럼.”

“아, 예.”

몇 번 더 꼬드길 줄 알았는데 바로 포기하네.

뭐, 나로서는 이야기가 빨리 끝나서 마음 편하다.

“그럼 이만.”

아직도 입을 봉인한 채 앉아 있는 혁무진을 툭 치며 자리에서 일어났다. 그때 월화가 묘한 웃음을 짓곤 말했다.

“아, 진 소협한테 전해 줄래요? 후원에 있는 노송(老松), 그거 비싼 거니까 수련 좀 조심히 해 달라고.”

산서성 제일의 정보 상인이 운영하는 객잔이다. 이곳에 들어온 후부터 내부 장기까지 훤히 읽히고 있는 거나 마찬가지겠지.

“그러죠.”

“필요한 거 있으면 말씀하시고. 우리 진 공자님 부탁인데 뭐든 다 구해 드려야지.”

눈을 찡긋거리는 그녀를 일별하고 방을 나오자마자 잠시 잊고 있던 일이 생각났다.

“무진아, 넌 왜 그렇게 주둥이를 함부로 놀리니?”

빡! 빡! 빡!

“악, 악, 악!”

한 명은 때리고, 한 명은 맞고.

그렇게 돌아온 별채에서는 반듯하게 잘려 나간 노송 몇 그루와 흡족한 얼굴의 진무경이 기다리고 있었다.

“베는 맛이 있군.”

“…….”

“…….”

언젠가 저놈을 베어 버리고 싶다.



* * *



고요해진 객실. 한동안 곰방대만 피워 물던 월화가 입을 연 것은 진태경이 떠나고 한참 후였다.

“내가 일전에 지시한 거, 알아봤어?”

객실 밖에서 대기하고 있던 하오문도가 낮은 목소리로 대답했다.

“나흘 전에 확인하신 것이 전부입니다. 추가 정보를 수집하고는 있습니다만…….”

“더 나올 게 없다?”

“예, 희박합니다.”

“희박? 그럼 가능성이 없진 않네? 계속 파. 시간 넉넉하게 줄 테니까 서두르지 말고. 지금 태원진가 건드렸다가는 우리도 좋은 꼴 못 보는 거 알지?”

“존명.”

물러가려는 하오문도를 붙잡은 건 이어지는 월화의 한마디였다.

“삼류 망나니가 불과 두 달도 안 돼서 산서잠룡이 됐어. 네 생각은 어때?”

“가능합니다. 소문대로라면.”

“아, 그거.”

월화가 피식 실소를 터트렸다. 진태경이 일문일살 조필을 쓰러트린 후부터 퍼지기 시작한 소문이다.

지금까지 진태경이 보인 모습은 모두 위장이었고, 사실은 그가 어린 시절부터 전폭적인 지원 아래 무공을 익혔다는 소문.

이제는 산서성 전역에 모르는 사람이 없을 정도로 퍼진 이야기다.

“그걸 믿니?”

“황당무계한 헛소문이죠. 하지만…….”

“사람들은 믿지. 멍청해서가 아니라, 믿을 수밖에 없으니까. 하지만 우리는 아니야.”

산서는 이미 중원에서 취급도 안 해 주는 변방이지만 하오문은 끊임없이 정보를 모아 왔다.

산서성의 유력가인 태원진가의 직계에 대해서는 말할 것도 없다. 유일한 실수라고는 혼란스러웠던 전란(戰亂)의 시기에 활동했던 대장로를 정확히 파악하지 못했다는 것뿐.

그러나 진태경에 관한 정보는 완벽에 가깝다.

“술, 여자, 도박. 어린 시절부터 나태했고 노는 것에만 정신이 팔려 있었지. 태원진가 역사에 저런 자가 있었나 싶을 정도로.”

“이 년 전, 지부장님께서 부임하시자마자 내린 첫 지시도 그것이었죠.”

“맞아. 산서 전체 동향 파악. 그리고 진태경 집중 조사.”

본디 재능은 대물림되는 법이다. 태원진가의 직계는 대대로 뛰어난 무재(武才)의 소유자들이었고 기인이라 평가받는 현 가주와 두 아들도 예외는 아니었다.

그 사이에서 진태경의 존재는 이질적일 만큼 눈에 띄었고, 그래서 하오문은 조사에 착수했다.

“결과는 허무했지.”

“정말 보이는 그대로 나왔습니다.”

가문의 핏줄 덕분인지 근골과 근맥이 약간 뛰어나다는 것 빼고는 특별할 것도 없었다.

“그때 뭔가 놓쳤던 걸까?”

“이틀에 한 번꼴로 기루에서 자고 가던 놈입니다. 잠을 줄여 가며 익혀도 부족한 것이 무공이지 않습니까?”

“알지, 잘 알지.”

월화는 일류 중에서도 제법 완숙한 경지까지 무공을 익힌 사람이다. 그에 대해 모를 리 없었다.

답답함에 연신 곰방대만 빨아들이던 그녀가 긴 숨을 토했다.

“결국 답은 하나뿐이네.”

“그렇습니다.”

진태경이 두 달 남짓한 시간 동안 삼류에서 초일류의 고수가 되었다는 것. 월화는 스스로 내린 결론에 기가 찼지만 어쩔 도리가 없었다.

“아까 내린 지시는 없던 걸로 해. 그에 대해서는 더 이상 묻지도, 알려고 하지도 마. 혹여나 입에 올리는 일 없도록 함구령 내리고.”

“존명. 단단히 일러두겠습니다.”

“아, 그리고 하나 더. 내일 일찍 떠날 테니까 준비해 둬.”

“누구를 데려가실 생각인지.”

“나 혼자.”

“지부장님, 그건…….”

“명령이야.”

“……존명.”

수하가 물러나자 객실에는 적막이 내리깔렸다. 월화는 까맣게 타 버린 담뱃잎을 털며 생각했다.

‘진태경이라.’

지금까지의 행보가 모두 사실이라면, 항산검문에게서 얻어 내야 할 북부 이권 따위는 아무것도 아니다.

‘고금을 통틀어 이 정도로 빠르게 성장한 이가 있었을까?’

진태경이 앉아 있던 자리를 바라보는 그녀의 눈빛이 깊게 가라앉았다.



* * *



다음 날 아침.

문제가 터졌다고 느낀 건 별채를 담당하는 책임자를 만난 후부터였다.

“숙박비 스물다섯 냥, 음식값 다섯 냥, 그리고 기물 파손비로 오십 냥. 총합 은자 여든 냥입니다.”

어제 마적 놈들을 주머니를 털었다며 희희낙락하던 혁무진이 입을 딱 벌렸다.

“기물 파손? 은자 오십 냥?”

“후원에 가 보니 노송 다섯 그루가 쓰러져 있더군요.”

월화가 비싸다고 했던 그 나무다.

나와 혁무진이 동시에 고개를 돌렸다. 시선이 마주친 진무경이 움찔하더니 입을 열었다.

“검을 펼치다 보니 흥에 취했다.”

“……아니, 시바. 흥에 취하면 걸리는 거 다 잘라도 되는 거야? 어?”

“후우우.”

혁무진은 뭐라 말은 못 하고 분노의 한숨만 푹푹 내쉬었다.

척 보아하니 내야 할 돈이 경비를 초과한 게 분명하다. 그래도 약간 정도라면 잘 말해서 협의점을 찾을 수도…….

“무진아, 지금 얼마 있냐?”

“사십 냥이요.”

협의점은 염병. 턱도 없네.

“혹시 외상 됩니까?”

별채 책임자의 입가에 맺혀 있던 상냥한 미소가 사라진 그 순간이었다.

“진 공자, 여기서 뭐 해요?”

이쪽을 향해 다가오는 하늘하늘한 궁장 차림의 미녀.

지금의 우리에게 있어 월화의 등장은 구명줄이나 다름없었다.

어젯밤 그녀의 제안을 단호하게 제안한 게 마음에 걸리지만, 이것저것 가릴 때가 아니다.

“아니, 그게요…….”

사정을 설명하자 월화가 눈을 동그랗게 떴다.

“여든 냥? 그럴 리가 없는데.”

“그렇죠? 좀 잘못된 것 같다니까요.”

“그거 이리 줘 봐.”

책임자가 들고 있던 죽간을 건네받아 읽기 시작하는 그녀.

점점 눈살을 찌푸리는 걸 보니 계산이 단단히 틀어진 것이 분명했다.

‘그럼 그렇지.’

이윽고 죽간을 모두 읽은 월화의 입술 사이로 싸늘한 목소리가 흘러나왔다.

“일 똑바로 안 해?”

“죄, 죄송합니다.”

“이분들이 어떤 분들이신데 감히 이따위 짓거리를…… 가격 똑바로 적어.”

혁무진이 작은 목소리로 소곤거렸다.

“천만다행이네요.”

“그러게. 접시 닦고 갈 뻔했네.”

“이공자님 때문에 뭔 고생입니까, 이게.”

“저 인간 얘기는 꺼내지도 마. 듣기만 해도 암 걸려.”

“암이 뭔데요?”

“……있어, 안 좋은 거.”

그사이 진땀을 흘려 가며 가격을 고친 책임자가 허리를 푹 숙이며 우리에게 사과했다.

“죄송합니다. 제가 생각이 짧아서 결례를 저질렀습니다.”

혁무진이 거만한 태도로 인사를 받았다.

“다음부턴 그러지 마쇼. 상대를 봐 가면서 장난을 쳐야지. 그래서 얼마요?”

“은자 백오 냥 하고도 철전 이십삼 냥입니다.”

“……?”

“……?”

뭐야, 이거. 꿈인가?

고개가 저절로 월화를 향해 돌아간다.

“무슨 소리예요, 저게?”

“내 지인이라고 멋대로 가격을 깎았더라고요. 감히 대태원진가의 자제분들을 뭘로 보고. 다시 한번 사과드려.”

“몰라뵈어서 죄송합니다!”

“그…….”

나는 잔뜩 목멘 목소리로 물었다.

“외상은 되죠? 당연히.”

“안 되죠. 당연히. 이 년 동안 단 한 번도 없었어요.”

“이번 기회에 선례를 남기는 건 어떨까요?”

“아직은 그럴 생각이 없어서. 다음 기회를 노려 봐야죠.”

월화가 화사한 웃음과 함께 덧붙였다.

“더 하실 말씀이라도?”

“……하, 항산.”

“뭐라고요?”

나는 눈을 질끈 감고 말을 이었다.

“항산검문까지 같이 가실래요?”

“와아, 저야 좋죠.”

저 가증스러운 웃음이라니. 월화의 손짓에 책임자가 죽간을 들고 빛의 속도로 사라진다.

“앞으로 여비 걱정은 없겠네요.”

혁무진처럼 현실을 받아들이는 사람이 있는 반면에, 결사반대를 외치는 사람도 있었다.

“헛소리! 가문의 임무를 수행하는 길에 어찌 여인을 데려간단 말이냐!”

“그럼 여기서 그릇 닦고 오든가.”

“…….”

“이 중에서 노송 자른 사람 손?”

진무경은 손을 들지 않았고, 월화는 그에게 치맛자락을 살짝 들어 올리며 인사했다.

“잘 부탁드려요. 진 소협.”
```

## Final English reading copy

```markdown
# Chapter 106

“Let’s go together. To the Mount Heng Sword Sect.”

“What?”

“You heard me, Young Master Jin. I have business at the Mount Heng Sword Sect too.”

“What kind of business?”

“I don’t think I can tell you that. I’m rather clear about keeping business and personal matters separate.”

*Talk about getting paid back tenfold.*

What I had just said had come back to bite me. Wolhwa’s smile deepened as she watched me grow awkward.

“I’m only joking. I happen to have something to collect from the Mount Heng Sword Sect. More precisely, something I’m supposed to receive from the Jin Family of Taiyuan.”

“What… Oh.”

A memory suddenly came to me. Back when the war with the Mount Heng Sword Sect was in full swing, the Jin Family of Taiyuan and the Lower District Sect had made a secret pact.

*Hadn’t we promised to give them ownership of the Mount Heng Sword Sect’s properties and such in exchange for information?*

The Lower District Sect—or rather, Wolhwa—had kept her promise. It was thanks to her help that we had been able to annihilate the Mount Heng Sword Sect’s vanguard in the early days of the war.

The Jin Family of Taiyuan had continued receiving help from the Lower District Sect afterward and had eventually won the war, but that was when the trouble began.

“As you know, Young Master Jin, our position has become rather awkward. We won the war, but we can’t lay our hands on the spoils.”

The strong devouring the weak. That was the law of Murim.

But the appearance of the Head Elder had ruined everything. The moment it came to light that the Jin Family of Taiyuan and the Mount Heng Sword Sect had both been manipulated by him, the justification for claiming the spoils had grown faint.

*So that’s why we’re pursuing a merger.*

Now was the time to put away our swords and negotiate with a brush. Jin Wikyung’s vision was to quietly and amicably absorb the Mount Heng Sword Sect within limits that would keep the world from condemning us.

Wolhwa wanted to receive her reward before that happened.

“If the Mount Heng Sword Sect accepts our proposal, couldn’t you demand your reward then?”

“That would only be possible if the Jin Family of Taiyuan were Shanxi’s hegemon rather than its Alliance Leader. If we tried to snatch things away carelessly in the current situation, the other mid-sized and small sects would withdraw too. And on top of that…”

For a moment, she looked at me with meaningful eyes before shaking her head.

*What was that supposed to mean?*

“And on top of that, what?”

“No, it’s nothing. Anyway, I did receive a proposal from the Lesser Family Head.”

Wolhwa took a puff from her long-stemmed tobacco pipe before continuing.

“He said he would transfer wealth equivalent to what he had promised, or hand over some of the areas managed by the Jin Family of Taiyuan.”

That sounded like a reasonable offer, but it looked different when viewed from the perspective of someone leading an organization rather than acting as an individual.

*She wants to expand her territory.*

Wolhwa’s true nature was neither that of a courtesan nor an innkeeper. She was an information merchant.

There was no doubt that she wanted to use this opportunity to expand the Lower District Sect’s influence into northern Shanxi, where it had been relatively weak because of the Mount Heng Sword Sect’s blockade.

*Jin Wikyung, naturally, wants the Jin Family of Taiyuan to encompass all of Shanxi.*

The Jin Family of Taiyuan had already wielded enormous influence over central and southern Shanxi for a long time. Handing over a few prime areas wouldn’t diminish the influence they had built up until now.

*This is exactly like a redevelopment district.*

The Mount Heng Sword Sect, which had held a firm grip on the north and blocked outside forces from entering, was collapsing. The greenbelt had been lifted and the area had become open for redevelopment, so the tug-of-war between Jin Wikyung and Wolhwa had begun.

*They’re both something else.*

Yesterday’s ally had become today’s competitor.

Once again, I felt that people were never everything they appeared to be.

“So I thought I’d meet our adorable new Sect Leader and collect what I’m owed while I was at it. How about we travel to the Mount Heng Sword Sect together?”

I answered without needing to think any further.

“I’ll have to decline.”

“Wow, aren’t you being a little too decisive? You cut me off without even hearing the terms.”

“As his younger brother, I can’t go around splashing filth on my hyung’s path.”

We weren’t related by blood, but I had long since accepted his existence—and this Murim—as my own.

“Hmm.”

Wolhwa stared at me for a moment before setting her pipe down with a sharp tap.

“All right, then.”

“Ah. Yes.”

I had expected her to tempt me a few more times, but she gave up right away.

Well, at least the conversation had ended quickly. That made things easier for me.

“Then we’ll be going.”

I gave Hyuk Mujin, who was still sitting there with his mouth sealed shut, a light tap and rose from my seat. That was when Wolhwa smiled strangely and spoke.

“Oh, could you tell Young Hero Jin something for me? The old pine in the rear courtyard is expensive, so please be careful with your training.”

This was an inn run by the greatest information merchant in Shanxi. Ever since we entered this place, she had probably seen right through us, down to our innards.

“Sure.”

“And tell me if you need anything. It’s a request from our Young Master Jin, so I have to procure anything you might need.”

She gave me a wink. I merely glanced at her and left the room, only to remember something I had momentarily forgotten.

“Mujin, why do you run your mouth so carelessly?”

Whack! Whack! Whack!

“Argh! Argh! Argh!”

One of us hit, and the other took the hits.

When we returned to the private residence, we found several old pine trees neatly cut down and Jin Mukyung waiting with a satisfied expression.

“There’s a certain satisfaction to cutting.”

“……”

“……”

*One day, I really want to cut that bastard down.*

* * *

The guest room had grown quiet. Wolhwa smoked her long-stemmed tobacco pipe for a long while before finally speaking, long after Jin Taekyung had left.

“Did you look into what I instructed you to investigate?”

A member of the Lower District Sect, who had been waiting outside the guest room, answered in a low voice.

“What you confirmed four days ago is all we have. We’re still gathering additional information, but…”

“Nothing else is going to turn up?”

“It’s unlikely.”

“Unlikely? Then there’s still a chance. Keep digging. I’ll give you plenty of time, so don’t rush. You know that if we provoke the Jin Family of Taiyuan right now, we won’t fare well either.”

“Yes, Branch Leader.”

The Lower District Sect member was about to withdraw when Wolhwa stopped him with one more question.

“A Third Rate wastrel became the Sleeping Dragon of Shanxi in less than two months. What do you think?”

“It’s possible, if the rumors are true.”

“Ah, that.”

Wolhwa let out a short laugh. It was a rumor that had begun spreading after Jin Taekyung defeated Jopil, One Question, One Kill.

According to the rumor, everything Jin Taekyung had shown until now had been an act. In truth, he had learned martial arts since childhood under the full support of the family.

By now, the story had spread throughout Shanxi to the point that there was hardly anyone who hadn’t heard it.

“Do you believe it?”

“It’s ridiculous nonsense. But…”

“People believe it. Not because they’re stupid, but because they have no choice but to believe it. But we’re different.”

Shanxi was already a frontier region that the Central Plains hardly even acknowledged, but the Lower District Sect had continued gathering information there without pause.

When it came to the direct descendants of the Jin Family of Taiyuan, one of Shanxi’s most powerful families, there was no need to mention it. Their only mistake had been failing to accurately assess the Head Elder, who had been active during the chaotic period of war.

But their information on Jin Taekyung was nearly perfect.

“Alcohol, women, gambling. He had been lazy since childhood and obsessed with nothing but having fun. He was so out of place that you would have wondered whether someone like him had ever existed in the history of the Jin Family of Taiyuan.”

“That was the first order you gave after taking office as Branch Leader two years ago.”

“That’s right. Monitor the entire situation in Shanxi. And investigate Jin Taekyung in depth.”

Talent was normally passed down through the generations. The direct descendants of the Jin Family of Taiyuan had possessed exceptional martial talent for generations, and the current Family Head and his two sons, all regarded as eccentrics, were no exception.

Jin Taekyung’s existence stood out so sharply among them that he seemed almost alien. That was why the Lower District Sect had begun its investigation.

“The result was anticlimactic.”

“He was exactly what he appeared to be.”

Other than having slightly superior bones and meridians, perhaps thanks to his family bloodline, there had been nothing special about him.

“Did we miss something back then?”

“He was the kind of bastard who spent the night at a pleasure house every other day. Martial arts already demands more time than a person has, even if they cut back on sleep.”

“I know. I know very well.”

Wolhwa had cultivated her martial arts to a fairly mature stage of the First Rate realm. There was no way she didn’t understand that.

She continued drawing on her pipe, exhaling long breaths in frustration before finally letting out a deep sigh.

“In the end, there’s only one answer.”

“That’s right.”

Jin Taekyung had gone from Third Rate to a master beyond First Rate in a little over two months. Wolhwa was dumbfounded by the conclusion she had reached herself, but there was nothing she could do about it.

“Cancel the order I gave earlier. Don’t ask about him anymore, and don’t try to find out anything else. Issue a gag order so that no one even mentions him.”

“Yes, Branch Leader. I’ll make sure they understand.”

“Oh, and one more thing. I’ll be leaving early tomorrow, so prepare everything.”

“Who are you planning to take with you?”

“No one. I’ll go alone.”

“Branch Leader, that…”

“It’s an order.”

“Understood.”

Once her subordinate withdrew, silence settled over the guest room. Wolhwa shook the completely burned tobacco leaves from her pipe and thought.

*Jin Taekyung.*

If everything he had done until now was true, then the northern interests she was supposed to extract from the Mount Heng Sword Sect were nothing.

*Has anyone in all history ever grown this quickly?*

Her gaze, fixed on the place where Jin Taekyung had been sitting, sank into deep contemplation.

* * *

The next morning.

I began to feel that something had gone wrong after meeting the person in charge of the private residence.

“The lodging fee is twenty-five nyang, the food comes to five nyang, and the property damage fee is fifty nyang. The total is eighty silver nyang.”

Hyuk Mujin, who had been rejoicing yesterday over emptying the pockets of those mounted bandits, gaped.

“Property damage? Fifty silver nyang?”

“When I went to the rear courtyard, I found that five old pine trees had fallen.”

They were the trees Wolhwa had said were expensive.

Hyuk Mujin and I turned our heads at the same time. Jin Mukyung, whose eyes met ours, flinched before opening his mouth.

“I got carried away while practicing my swordsmanship.”

“……No, fuck. If you get carried away, does that mean you can cut down anything in your way? Huh?”

“Hoooo.”

Hyuk Mujin couldn’t say anything. He merely kept letting out furious sighs.

At a glance, it was obvious that the bill exceeded the amount we had on hand. If it had only been a little over, we might have been able to talk things out and find a compromise…

“Mujin, how much money do you have right now?”

“Forty nyang.”

*To hell with a compromise. We’re nowhere close.*

“Could we put it on credit?”

That was the exact moment the kind smile around the private-residence manager’s lips disappeared.

“Young Master Jin, what are you doing here?”

A beautiful woman in a light, flowing palace-style dress was approaching us.

Wolhwa’s appearance was nothing short of a lifeline.

I felt bad about turning down her proposal so decisively the night before, but this was no time to be picky.

“Well, you see…”

When I explained the situation, Wolhwa’s eyes grew round.

“Eighty nyang? That can’t be right.”

“Exactly. I knew something was wrong.”

“Give me that.”

She took the bamboo slip from the manager and began to read.

The deeper her frown grew, the clearer it seemed that the arithmetic had been badly botched.

*Knew it.*

At last, Wolhwa finished reading the bamboo slip. A chill entered her voice.

“Are you not doing your job properly?”

“I-I’m sorry.”

“Who do you think these gentlemen are, to dare pull this kind of stunt? Write the prices correctly.”

Hyuk Mujin whispered in a small voice.

“What a relief.”

“Yeah. We almost had to wash dishes before leaving.”

“What kind of hardship is this because of the Second Young Master?”

“Don’t even mention that man. Just hearing about him gives me cancer.”

“What’s cancer?”

“……It’s something bad.”

Meanwhile, the manager revised the prices while sweating profusely. Then he bent deeply at the waist and apologized to us.

“I’m sorry. I was thoughtless and committed a grave discourtesy.”

Hyuk Mujin accepted the apology with an arrogant air.

“Don’t do that again. You have to know who you’re dealing with before pulling a prank. So how much is it?”

“One hundred and five nyang, along with twenty-three iron coins.”

“……”

“……”

*What the hell? Is this a dream?*

My head turned toward Wolhwa of its own accord.

“What is that supposed to mean?”

“He arbitrarily lowered the price because you were my acquaintances. How dare he take the young masters of the Jin Family of Taiyuan for fools? Apologize to them again.”

“I’m sorry for failing to recognize your identities!”

“But…”

I asked in a thoroughly choked voice.

“We can put it on credit, right? Of course.”

“No, you can’t. Of course not. We haven’t allowed that even once in the past two years.”

“How about making an exception and setting a precedent this time?”

“I don’t have any plans to do that yet. You’ll have to aim for the next opportunity.”

Wolhwa added with a bright smile,

“Was there something else you wanted to say?”

“……M-Mount Heng.”

“What was that?”

I squeezed my eyes shut and continued.

“Would you like to come with us to the Mount Heng Sword Sect?”

“Wow, I’d love to.”

*That hateful smile.*

At Wolhwa’s gesture, the manager snatched up the bamboo slip and vanished at the speed of light.

“We won’t have to worry about travel expenses anymore.”

While Hyuk Mujin was the sort of person who simply accepted reality, someone else was shouting vehement opposition.

“Nonsense! How can you bring a woman along while carrying out a family mission?”

“Then stay here and wash dishes.”

“……”

“Who here cut down the old pine trees? Raise your hand.”

Jin Mukyung didn’t raise his hand. Wolhwa slightly lifted the hem of her skirt and greeted him.

“Please take good care of me, Young Hero Jin.”
```
