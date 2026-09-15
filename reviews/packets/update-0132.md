<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0132.txt",
      "sha256": "52a1483da9f4f49765f3b8fb28454d61c613c8338b99d80ab57c8865bcb4ab9e",
      "bytes": 13899
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b43aeab5aa3b51a79fbe54de2c452623410b64cc1784d6cf052f5e52e5174a72",
      "bytes": 7026
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9a05623706ab206f7762524bf168615543f755f01e18a213052ea846a53f0de8",
      "bytes": 24226
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "bd8f15897af1241f2b078dff597c3cab9db9d4fe8d526a78bacd6838525a48b8",
      "bytes": 486
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "592ff6e535fa71f359d32b6a635dd8383f4aa91c05e9910d8f46c44b7a551767",
      "bytes": 5353
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "6220d12840192d181c499c3061e0bda38b155dc94cb4c9cf67617579b874ce41",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8656b73cee6f1cb7122322c0e158f42079ad8abfd2ba1acb6ee60edd70df99ee",
      "bytes": 24583
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "38334c666addb3824240d3460030e2b1e1a16a71f0e64f78160b6f42a59d7285",
      "bytes": 20709
    }
  ],
  "estimated_tokens": 22345
}
-->

# Durable State Update — Chapter 132

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 132. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 132. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 132,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 132,
    "continuity_sources": [132],
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
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered.",
    "Cheol Mubaek remains severely injured and needs extended recuperation; Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect and vows to preserve it.",
    "The Lower District Sect sent a relief force after the battle; Wolhwa's real name is Eun Sowol, and she is its Shanxi Branch Leader.",
    "Lee Seowol accepted the Jin Family of Taiyuan's New Year invitation, offered the Mount Heng Sword Sect's territorial rights as an apology, and proposed marriage to Taekyung in exchange for three Peak martial arts; Taekyung plans to reject her because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty; it is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued Mount Heng.",
    "Cheol Mubaek and Lee Cheonbaek became close friends after first meeting and fighting more than thirty years ago; Cheol is the ninth-generation successor of the Shura Annihilating Fist.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; the Fire King and the status of the Fire Gate Clan's single successor remain unknown.",
    "The Temporary Strength Pill is in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers; the Jin Family displayed a large Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night for three days; Wipeng is called the God of Drinking and Taekyung is rumored to be the Night King.",
    "Taekyung's Sleeping Dragon of Shanxi Title effect strengthened to all stats +15 and Fame +200; his current Status Window shows Level 61, Fame 2,100 (+250), and 60 remaining points.",
    "Hyuk Mujin accepted The City Lord's Invitation, requiring attendance at the City Lord's luncheon with young prodigies tomorrow.",
    "The City Lord of Shanxi Province is a ten-year-old Prince and the Emperor's youngest brother, appointed at age five; Jin Mukyung met him after being summoned three years earlier and considered the encounter a nightmare.",
    "Seokchil is a middle-aged porter with nearly twenty years of experience at the Seongun Escort Bureau in southern Shanxi Province.",
    "Cheongpung is an eccentric former porter who recently fled Huashan's Lotus Peak and traveled toward Taiyuan; he has now appeared at Honghwa Inn with a ??? Level and the aura of another Peak master.",
    "Hyuk Mujin's parents are healthy textile merchants in Taiyuan who own the city's largest textile shop, with branches in Henan and Hebei; Mujin left home to avoid inheriting the business, and a younger sibling later removed that obligation.",
    "Taekyung has begun treating Hyuk Mujin as a valued companion rather than merely a subordinate, acknowledging the hardship Mujin endured while traveling with him."
  ],
  "continuity_sources": [
    131,
    130
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "What will happen at the City Lord's luncheon and how will the City Lord react to Taekyung?",
    "What was Cheongpung's status at Huashan's Lotus Peak, and why did he leave?"
  ],
  "safe_through": 131,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years of internal energy.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, 시진 as shichen, 표행 as escort run, 쟁자수 as porter, 표국 as Escort Bureau, 표두 as Escort Chief, 은원보 as silver ingot, 은자 as nyang of silver, 사서삼경 as the Four Books and Three Classics, and 연화봉 as Lotus Peak.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, 여포 as Lü Bu, 성주의 초청 as The City Lord's Invitation, 친왕 as Prince, 주씨 as Zhu, 천자 as Son of Heaven, 황상 and 황제 as Emperor, 태자 as Crown Prince, 구파일방 as Nine Sects and One Gang, and 오대세가 as Five Great Families.",
    "Render 빙당호로 as candied hawthorn skewers with an explanatory footnote; render 혁가 포목점 as Hyuk Family Textile Shop and 하북 as Hebei."
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
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |

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
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 산서     | **Shanxi**             |
| 공자      | **Young Master**                                                |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 131
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an apparent Peak master whose System Level is ???
- **Personality:** Affable, dreamy, hazy, and childlike in manner
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Unknown; approaches Jin Taekyung and Hyuk Mujin to ask for a candied hawthorn skewer

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 131
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; traveling as Jin Taekyung’s attendant for the City Lord’s luncheon
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 131
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 129
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

## Korean source

```text
＃132화



“실례가 안 된다면 빙당호로 하나만 먹어도 되겠습니까?”

예상을 뛰어넘는 멘트에 순간 뇌정지가 왔다.

‘이게 뭔 소리야.’

도를 아십니까도 아니고, 빙당호로 하나만 먹어도 되겠냐니.

처음 만난 절정 고수가 세상에서 가장 정중한 말투로 빙당호로를 구걸하는 상황은 내 계획에 없었는데.

꼬르륵.

이제는 배꼽시계로 측은지심까지 자극한다. 나는 엉겁결에 아직 들고 있던 빙당호로를 내밀었다.

“여, 여기요.”

“감사합니다, 은인.”

빙당호로 가성비 보소, 만난 지 10초 만에 절정 고수의 은인이 됐다.

애들이나 먹을 법한 사탕 과자를 맹렬하게 물고 빠는 청년, 청풍의 모습을 나와 혁무진이 멍하니 지켜봤다.

“조장님, 아는 사람이에요?”

“아니.”

빙당호로 하나를 게 눈 감추듯 먹어 치운 청풍은 아직 모자란지 굶주린 맹수의 눈빛으로 혁무진을 바라봤다.

정확히는 녀석의 양손에 들린 빙당호로 두 개를.

“……무진아.”

“네?”

“드려라.”

혁무진이 재빨리 손을 뒤로 감췄다.

“싫습니다.”

“싫어?”

“예, 저 이거 오 년 만에 처음으로 먹는 겁니다. 아직 입도 안 댔어요.”

“그렇구나. 우리 무진이가 예상 수명보다 오십 년 정도 일찍 죽고 싶구나.”

“…….”

한숨을 푹 내쉰 녀석이 빙당호로를 내밀자 청풍의 눈이 번쩍 빛났다.

“감사합니다, 은인!”

다음 순간, 휙 하는 바람 소리와 함께 빙당호로가 청풍의 손으로 옮겨 갔다.

“으헉.”

실로 엄청난 속도다. 헛숨을 들이킨 혁무진이 내게 떨리는 목소리로 속삭였다.

“보, 보통 거지가 아닌데요?”

눈앞의 꾀죄죄한 청년이 절정 고수라는 사실을 알면 무슨 표정을 지을까?

나는 정신없이 빙당호로를 흡입 중인 청풍을 유심히 살폈다.

‘절정 고수라기에는 너무 젊어 보이는데.’

나도 지금까지 주워들은 풍문이 있다. 명문 대파에서 온갖 영재 교육과 지원을 쏟아부어도 가물에 콩 나듯 탄생하는 것이 절정 고수라는 사실도 이제는 안다.

천하에서도 변방 촌구석 취급받는 산서성 출신인 진무경이 유명해진 이유도 그 때문이다.

남들보다 10년, 20년을 앞서 절정의 경지에 올랐으니까.

‘그런데…….’

기껏해야 내 또래로 보이는 녀석이 기감으로도 레벨을 파악하지 못하는 절정 고수라니.

산서성에 저렇게 젊은 절정 고수가 있다는 말은 들어 본 적이 없다.

‘이런 놈이 어디서 튀어나온 거지?’

때마침 청풍이 고개를 들었다. 허겁지겁 먹은 터라 입가에는 끈적끈적한 설탕이 한가득 묻어 있었다.

“휴우, 잘 먹었습니다.”

“배가 좀…… 많이 고프셨나 보네.”

“네. 하루 종일 굶었거든요.”

“저런, 어쩌다가?”

“여비를 잃어버리는 바람에 그만. 그래도 재미있는 경험을 했네요.”

“…….”

돈 없어서 온종일 쫄쫄 굶은 게 재밌는 경험이 될 수 있나?

처음 만난 그 순간부터 느낀 거지만 확실히 사고방식이 특이한 놈이다.

청풍이 해맑게 웃으며 꾸벅 포권을 취했다.

“아, 제 소개가 늦었네요. 은인들께 청풍이 인사 올립니다.”

“진태경이라고 합니다.”

“전 이분의 오른팔이자 심장, 혁무진입니다.”

혁무진의 헛소리를 깔끔하게 무시하고 청풍을 주시했다.

내가 이래 봬도 나름 산서성에서는 유명 인사다.

몇 달 전까지만 해도 나쁜 쪽으로, 지금은 정반대의 이유로 산서성에서 내 이름을 모르는 사람이 없다.

‘알아보려나?’

은근히 기대감을 품은 그때, 청풍의 얼굴이 딱딱하게 굳었다.

“저, 혹시…….”

“네, 맞습니다. 제가 바로 그.”

“실례가 안 된다면 좀 더 신세 져도 될까요?”

“예?”

“제가 좀 오래 굶어서.”

때맞춰 청풍의 배에서 천둥 같은 소리가 흘러나왔다.

꼬르륵.

“……그럼 같이 식사라도.”

“감사합니다, 은인!”

이게 은인인지 호구인지 모르겠다.



* * *



홍화객잔의 내부는 이른 저녁 식사를 하러 온 사람들로 바글거렸다.

발 빠르게 달려온 점소이가 몇 안 되는 빈자리로 우리를 안내해 주었다.

“음식은 뭘로 드릴깝쇼?”

나는 나무로 제작된 무림식 메뉴판을 청풍에게 건네줬다.

“드시고 싶은 거 시키세요.”

“아앗, 아닙니다. 제가 은혜도 모르는 금수(禽獸)도 아니고 어찌…….”

“괜찮으니까 드시고 싶은 거 시키세요.”

“그럼 여기 있는 거 전부 주세요.”

“…….”

이런 금수 같은 놈을 봤나.

대형 호구의 등장에 주방만 바빠졌다. 얼마 지나지 않아 주문한 음식들이 쉬지 않고 줄줄이 쏟아져 나왔다.

“산니백육(䔉泥白肉) 나왔습니다. 이 음식은 삶은 돼지고기를 얇게 포를 떠서…….”

“오.”

“어향육사(魚香肉絲) 나왔습니다. 돼지고기를 죽순, 목이버섯 등과 함께…….”

“오오.”

“경장육사(京醬肉絲)입니다.”

“오오오!”

“규화계(叫花鷄).”

“오오오오!”

처음에는 열심히 설명해 주던 점소이의 말이 점점 짧아지는 것과 달리, 청풍의 리액션은 갈수록 풍부해졌다.

끊임없이 탁자를 채워 가는 요리. 슬슬 음식을 놓을 자리가 없어질 때쯤 점소이가 현자 타임이 온 듯한 얼굴로 새로 나온 접시를 슥 내밀었다.

“매구.”

“매구?”

옆 동네 섬나라 사는 메구미는 알아도 매구는 처음 들어 본다. 내 시선에 점소이가 귀찮다는 듯이 대답했다.

“매채구육(梅采拘肉)이요.”

“…….”

이제는 하다 하다 줄임말까지 쓰는구나.

내가 어이없어하는 사이 청풍은 빠르게 음식 접시를 비워 나가고 있었다.

“우걱, 우걱.”

“천천히 드세요. 천천히.”

“아히헤호. 하후이흡히하.”

“……대답하지 말고 그냥 드세요.”

“캉사합히하!”

혁무진이 입맛이 뚝 떨어진 얼굴로 속삭였다.

“진짜 거지 아닙니까?”

“아까 빙당호로 낚아채는 거 못 봤어? 절대 아니야.”

“쿰척, 쿰척!”

“……아마도 아닐 거야.”

“혹시 압니까, 개방(丐幫)의 고수일지도.”

“개방이라.”

무협 소설에서 질리도록 많이 봤다. 실제로 현 무림에도 구파일방(九派一幇) 중 하나로 버젓이 존재한다.

아직 만나 보지는 못했지만, 당장 저기 객잔 입구에서 어슬렁거리는 거지 중 하나가 개방도일 수도 있다.

“제가 매듭 있나 살짝 확인해 볼까요?”

개방의 고수들은 허리의 매듭으로 신분을 구별한다던가?

나는 고개를 저었다.

‘아니, 일단 개방 소속은 아니야.’

그렇다면 내 이름을 들었을 때 어떻게든 반응이 왔을 거다. 같은 정파 소속이니 일부러 모른 척할 이유도 없고.

‘그럼 어느 문파 출신이지?’

이렇게 젊은 절정 고수가 하늘에서 뚝 떨어졌을 리는 없다.

최소한 이름난 문파 출신일 텐데……. 갈수록 이 수수께끼의 청년에 대한 호기심이 샘솟는다.

“꺼윽, 잘 먹었습니다.”

마침내 식사를 끝마친 청풍이 올챙이배를 두드리다가 나와 혁무진을 보고 멈칫했다.

“다 처음 먹어 보는 음식이라 은인들 앞에서 추태를 보였습니다. 제가 너무 과하진 않았는지…….”

이미 충분히 과했어, 인마.

그래도 최소한의 자각이라도 있어서 다행이다.

“괜찮습니다. 저도 가끔 그러는데요 뭘.”

“저랑 통하는 구석이 있으시네요. 하하.”

나는 청풍을 따라 웃으며 입을 열었다. 이제 슬슬 호구 조사를 시작할 타이밍이다.

“그런데 다 처음 먹어 보는 음식이라니, 평소에 기름진 음식을 잘 안 드시는 모양이네요.”

청풍이 침울하게 고개를 내저었다.

“안 먹는 게 아니라 못 먹었어요. 이렇게 맛있는 음식들이 있는 걸 알았다면 좀 더 일찍 하산했을 텐데.”

“아아, 산에 사셨구나. 많이 힘드셨겠네.”

“산 생활이요? 재밌어요. 경치도 좋고, 여기저기 먹을 것도 많고요. 저희 할아버지도 산에서 평생 혼자 사셨는걸요.”

“할아버님이요?”

“예. 그런데 저어…….”

“말씀하세요.”

“술 좀 시켜도 될까요? 제가 아직 술을 못 먹어 봐서.”

“……얼마든지 시키세요.”

이 자식은 못 먹어 본 것도 많네.

그래도 한 줄기 양심은 남아 있는지 가장 값싼 화주 한 병을 시킨다.

잠시 후, 화주를 거침없이 들이킨 청풍이 약간 붉어진 얼굴로 중얼거렸다.

“으아, 이게 취한다는 거구나. 그런데 우리가 무슨 얘기를 하고 있었죠?”

“할아버님께서 산에서 평생 혼자 사셨다는 것까지.”

“아, 맞다. 아무튼, 저도 어릴 때부터 할아버지랑 같이 살았어요. 그게 다섯 살 때부터니까, 벌써 십오 년이나 됐네요.”

“그래요? 진짜 오래됐네.”

나는 놀란 티를 내지 않으려고 애썼다.

불과 약관에 절정 고수라니. 최소한 진무경에 버금가거나 그 이상 가는 천재란 소리다. 이야기를 나눌수록 그의 정체가 점점 궁금해졌다.

“거기가 어디예요? 그렇게 살기 좋은 곳이면 나중에 한번 놀러 가 볼까 하는데.”

뭔가 말하려던 청풍이 순간 멈칫했다.

“어어, 그건 말씀 못 드릴 것 같은데.”

“에이, 그 정도도 말 못 해 줘요?”

“왜냐하면, 할아버지가 엄청나게 싫어하셔서…… 안 그래도 그것 때문에 일 년에 한두 번씩은 거처를 옮기시거든요.”

“거처를 옮겨요?”

“네. 자꾸 이상한 사람들이 찾아와서요.”

이상한 사람들이라니. 진상 등산객인가?

하긴, 산에 사는 사람한테는 불편할 만도 하겠다.

그가 추억에 잠긴 눈으로 말을 이었다.

“제가 열 살 때였는데, 어느 날 수십 명이 우르르 찾아와서 행패를 부리는 거예요. 할아버지께서 산에 불 질러 버리기 전에 꺼지라고 소리치시던 기억이 나요.”

“아, 그래서 계속 거처를 옮기시는……?”

“네, 다행히 산이 넓어서 십 년째 잘 피해 다니고 계세요.”

“…….”

십 년씩이나? 그 할아버지도 대단한 양반이다.

그때 청풍의 이야기를 흥미진진하게 듣고 있던 혁무진이 물었다.

“그럼 공자께서는 왜 하산하신 겁니까?”

아쉬운 듯이 술병 주둥이를 쪽쪽 빨던 청풍이 대답했다.

“십봉룡(十鳳龍) 때문에요.”

“십봉룡? 그건 또 뭐야?”

내 물음에 혁무진이 별 이상한 놈 다 본다는 눈빛으로 대답했다.

“조장님이 십봉룡을 왜 몰라요?”

“모를 수도 있지, 인마.”

“엥? 작년에 기루에서 술 푸지게 먹고 십봉룡이 될 거라고 떠들었다가 개망신당했으면서.”

“그건 내가 아니라…… 됐다. 그래서 십봉룡이 뭔데?”

“진심으로 몰라서 물어보시는 겁니까?”

“모르면 안 되냐?”

“당연히 안 되죠. 당장 이공자님이 십봉룡인데.”

어, 진짜?

눈을 깜빡거리는 내게 혁무진이 열변을 토했다.

“정파 무림 최고의 후기지수들! 차기 무림을 이끌어갈 용과 봉황들! 십봉룡을 모른다는 게 말이나 됩니까?”

“야, 야. 목소리나 줄여. 사람들 쳐다보잖아.”

그냥 하는 말이 아니라 혁무진의 쩌렁쩌렁한 외침 때문에 주위 손님들이 우리를 힐끗거리는 중이다.

“쳐다보면 뭐 어때요. 이건 조장님이 해도 너무하잖아요! 사람 놀립니까, 예?”

“사람 놀리는 건 모르겠고, 때리는 건 잘해.”

“제가 너무 흥분한 것 같네요. 죄송합니다.”

순식간에 이성을 되찾은 혁무진을 뒤로하고 청풍을 향해 사람 좋은 미소를 지어 보였다.

“말씀 계속하시죠.”

“별건 아니에요. 순간적으로 치기 어린 생각이 들었던 거죠.”

청풍이 살짝 풀린 눈으로 나를 응시했다. 굳이 공력으로 취기를 몰아내지 않을 생각인지 여전히 살짝 알딸딸한 모습이다.

“나와 저들 중에 누가 더 강할까? 저는 그 의문에 대한 답을 확인하고 싶었어요.”

결국은 무인의 호승심(好勝心) 때문이라는 거다.

새로운 세상으로 나아가고픈 마음, 강자를 꺾어 자신의 무공을 입증하고픈 마음이 그의 발걸음을 산 아래로 이끌었음을 짐작할 수 있었다.

‘저런 생각을 해도 될 만큼의 실력도 있는 것 같고.’

진무경은 약관에 절정의 경지에 올라 중원을 떠들썩하게 만들었다고 했다. 그랬던 그는 지금 십봉룡, 정파 최고의 후기지수 중 한 사람으로 꼽힌다.

눈앞의 청풍은 최소 진무경에 비견할 만한 무재(武才)의 소유자다.

‘그럴 만한 자격이 있어.’

내심 고개를 끄덕이던 그 순간이었다.

“푸하하하!”

“큭, 크큭. 아, 웃음 참느라 혼났네.”

소리의 근원지를 향해 고개를 들었다.

2층. 비단옷을 걸친 다섯 명의 남녀가 얼굴 가득 비웃음을 띤 채 우리를 내려다보고 있었다.
```

## Final English reading copy

```markdown
# Chapter 132

“If it wouldn’t be too much trouble, may I have just one candied hawthorn skewer?[^1]”

[^1]: Candied hawthorn skewers are a traditional Chinese snack made by coating skewered fruit in hardened sugar.

The unexpected comment caused my brain to freeze for a moment.

*What the hell is he talking about?*

It wasn’t one of those *Do you know the Way?* pitches. He was asking if he could have just one candied hawthorn skewer.

I hadn’t planned for a Peak master I’d just met to beg for candied hawthorn in the most polite tone in the world.

*Grrrrrrowl.*

Now he was even tugging at my pity with his stomach clock. Without thinking, I held out the candied hawthorn skewer I was still holding.

“H-here.”

“Thank you, Benefactor.”

Talk about value for money. Ten seconds after meeting him, I had become a Peak master’s Benefactor.

Hyuk Mujin and I stared blankly at Cheongpung as he ferociously bit and sucked on the candy-coated snack children usually ate.

“Captain, do you know him?”

“No.”

Cheongpung devoured the candied hawthorn skewer as though it had vanished in the blink of an eye. Apparently, it hadn’t been enough, because he turned toward Hyuk Mujin with the eyes of a starving beast.

More precisely, he stared at the two candied hawthorn skewers in Mujin’s hands.

“…Mujin.”

“Yes?”

“Give them to him.”

Hyuk Mujin quickly hid his hands behind his back.

“No.”

“You don’t want to?”

“Yes. This is the first time I’ve eaten these in five years. I haven’t even taken a bite yet.”

“I see. Our Mujin wants to die fifty years ahead of schedule.”

“…”

With a deep sigh, he held out the candied hawthorn skewers. Cheongpung’s eyes flashed.

“Thank you, Benefactor!”

The next moment, accompanied by a sharp *whoosh*, the candied hawthorn skewers had transferred into Cheongpung’s hands.

“Gah!”

That was an incredible speed. Hyuk Mujin sucked in a startled breath and whispered to me in a trembling voice.

“He’s not an ordinary beggar, is he?”

What kind of expression would Mujin make if he learned that the filthy young man in front of us was a Peak master?

I studied Cheongpung as he inhaled the candied hawthorn with single-minded focus.

*He looks far too young to be a Peak master.*

I had heard a few rumors by now. I also knew that even famous, powerful sects with every kind of genius training and support only produced a Peak master once in a blue moon.

That was why Jin Mukyung, who had come from Shanxi Province—a remote backwater even by the standards of the Central Plains—had become so famous.

*He reached the Peak realm ten or twenty years ahead of everyone else.*

*But…*

The young man in front of me looked barely my age, yet he was a Peak master whose Level I couldn’t even determine through Qi Sense.

I had never heard of a Peak master this young living in Shanxi Province.

*Where the hell did this guy come from?*

As if on cue, Cheongpung raised his head. Since he had eaten so hurriedly, his mouth was covered in sticky sugar.

“Whew. That was delicious.”

“You must’ve been a little… very hungry.”

“Yes. I haven’t eaten all day.”

“Oh dear. How did that happen?”

“I lost my travel expenses. Still, it was an interesting experience.”

“…”

Could being forced to starve all day because you had no money really count as an interesting experience?

I had felt it from the moment we met, but this guy definitely had a peculiar way of thinking.

Cheongpung smiled brightly and gave us a respectful fist-and-palm salute.

“Ah, I’m late introducing myself. Cheongpung offers his greetings to his Benefactors.”

“My name is Jin Taekyung.”

“I’m this man’s right arm and heart, Hyuk Mujin.”

I completely ignored Hyuk Mujin’s nonsense and kept my eyes on Cheongpung.

I might not look it, but I was fairly famous in Shanxi Province.

Until a few months ago, I had been famous for all the wrong reasons. Now, for the exact opposite reasons, there wasn’t a single person in Shanxi Province who didn’t know my name.

*I wonder if he’ll recognize me.*

Just as I was secretly getting my hopes up, Cheongpung’s face went stiff.

“Excuse me, are you perhaps…”

“Yes, that’s right. I’m the very—”

“Would it be all right if I imposed on you a little longer?”

“What?”

“I’ve been hungry for quite a long time.”

Right on cue, a thunderous sound came from Cheongpung’s stomach.

*Grrrrrrowl.*

“…Then why don’t we have a meal together?”

“Thank you, Benefactor!”

I couldn’t tell whether I was his Benefactor or just a sucker.

* * *

The inside of Honghwa Inn was packed with people who had come for an early dinner.

A quick-footed waiter led us to one of the few remaining empty tables.

“What’ll it be?”

I handed the wooden menu board to Cheongpung.

“Order whatever you want.”

“Oh, no, I couldn’t. I’m not some ungrateful beast who doesn’t know how to repay a kindness. How could I…”

“It’s fine. Order whatever you want.”

“Then I’ll have everything on here.”

“…”

What an ungrateful beast.

The appearance of a colossal sucker kept the kitchen busy. Before long, the dishes we had ordered began pouring out without pause.

“Garlic Pork is here. This dish is made by slicing boiled pork thin and…”

“Oh.”

“Fish-Fragrant Shredded Pork is here. It’s pork served with bamboo shoots, wood ear mushrooms, and…”

“Ohhh.”

“Beijing Sauce Shredded Pork.”

“Ohhhh!”

“Beggar’s Chicken.”

“Ohhhhh!”

Unlike the waiter, whose explanations had grown shorter and shorter, Cheongpung’s reactions were becoming more and more elaborate.

Dish after dish continued filling the table. Just as there was barely any room left, the waiter pushed out another plate with the expression of a man who had reached enlightenment.

“Maegu.”

“Maegu?”

I’d heard of Megumi from the island country next door, but Maegu was a new one to me. Catching my look, the waiter answered as if explaining it was a chore.

“Maechae Guyuk.”[^2]

“…”

Now he was even abbreviating dish names.

While I stared at him in disbelief, Cheongpung rapidly emptied the plates.

[^2]: *Maechae Guyuk* is pork belly with preserved mustard greens. The waiter shortens its Korean name to *Maegu*, which sounds like the beginning of the Japanese name Megumi.

“Nom, nom.”

“Slow down. Eat slowly.”

“Mmph, mmph. Ah hih he ho. Ha hu i heup hi ha.”

“Don’t answer. Just keep eating.”

“Khanks hah!”

Hyuk Mujin whispered with a thoroughly disgusted expression.

“Isn’t he really a beggar?”

“Didn’t you see him snatch the candied hawthorn earlier? He definitely isn’t.”

*Chomp, chomp.*

“…Probably.”

“What if he’s a master of the Beggars’ Sect?”

“The Beggars’ Sect, huh?”

I had seen it countless times in martial arts novels. It also existed openly in the actual Murim as one of the Nine Sects and One Gang.

I had never met one of its members, but any of the beggars loitering near the inn’s entrance could be a Beggars’ Sect disciple.

“Should I take a quick look to see whether he has any knots?”

The masters of the Beggars’ Sect supposedly distinguished their status by the knots around their waists.

I shook my head.

*No. He isn’t with the Beggars’ Sect.*

If he were, he would have reacted somehow when he heard my name. We belonged to the same orthodox faction, so he had no reason to pretend he didn’t recognize me.

*Then what sect is he from?*

There was no way a Peak master this young had simply dropped out of the sky.

He had to come from a famous sect at the very least… The more I thought about it, the more curious I became about this mysterious young man.

“Burp. That was delicious.”

Cheongpung finally finished eating. After patting his tadpole-like belly, he looked at Hyuk Mujin and me, then stopped short.

“It was my first time trying any of these dishes, so I made a spectacle of myself in front of my Benefactors. I hope I didn’t overdo it…”

*You were more than excessive, you idiot.*

Still, it was good that he had at least a little self-awareness.

“It’s fine. I do that sometimes, too.”

“We have something in common. Ha-ha.”

I laughed along with Cheongpung and opened my mouth. It was time to start questioning him.

“You said everything was your first time eating it. You don’t usually eat rich food, do you?”

Cheongpung shook his head gloomily.

“It’s not that I don’t eat it. I couldn’t eat it. If I’d known food this delicious existed, I would have come down from the mountain sooner.”

“Oh, so you lived in the mountains. That must have been difficult.”

“Life in the mountains? It was fun. The scenery was beautiful, and there was plenty to eat here and there. My grandfather has lived alone in the mountains his entire life, too.”

“Your grandfather?”

“Yes. But, um…”

“Go ahead.”

“May I order some alcohol? I’ve never had any before.”

“…Order as much as you like.”

This kid had a lot of things he had never tried.

At least he still had a sliver of conscience left. He ordered the cheapest bottle of fire liquor.

A short while later, Cheongpung downed the fire liquor without hesitation and muttered with a slightly flushed face,

“Ahh, so this is what it means to get drunk. But what were we talking about?”

“That your grandfather had lived alone in the mountains his entire life.”

“Oh, right. Anyway, I lived with my grandfather from a young age. That started when I was five, so it’s already been fifteen years.”

“Really? That’s a long time.”

I did my best not to show my surprise.

*A Peak master at barely twenty.*

That meant he was a genius at least comparable to Jin Mukyung, if not greater. The more I talked with him, the more curious I became about his identity.

“Where was it? If it’s such a nice place to live, maybe I could visit sometime.”

Cheongpung hesitated just as he was about to say something.

“Um, I don’t think I can tell you that.”

“Come on. You can’t even tell me that much?”

“Because my grandfather hates it when people visit. He moves to a different place once or twice a year because of that.”

“He moves?”

“Yes. Strange people keep coming to see him.”

*Strange people? Obnoxious hikers?*

Well, I suppose it would be annoying for someone living in the mountains.

He continued speaking with a nostalgic look in his eyes.

“When I was ten, dozens of people suddenly came rushing over and started causing trouble. I remember my grandfather shouting at them to get lost before he set the mountain on fire.”

“Oh, so that’s why he keeps moving?”

“Yes. Fortunately, the mountains are huge, so he’s been avoiding them successfully for ten years.”

“…”

Ten years? His grandfather was quite a man.

Hyuk Mujin, who had been listening to Cheongpung’s story with great interest, asked,

“Then why did Young Master come down from the mountain?”

Cheongpung, who had been sucking on the mouth of the liquor bottle regretfully, answered,

“Because of the Ten Dragons and Phoenixes.”

“The Ten Dragons and Phoenixes? What’s that supposed to be?”

At my question, Hyuk Mujin looked at me as though I were the strangest person he had ever seen.

“Why don’t you know about the Ten Dragons and Phoenixes, Captain?”

“I’m allowed not to know, damn it.”

“Huh? You made a complete fool of yourself last year after getting plastered at a pleasure house and bragging that you were going to become one of them.”

“That wasn’t me… Never mind. What are the Ten Dragons and Phoenixes?”

“Are you seriously asking because you don’t know?”

“Can’t I just not know?”

“Of course you can’t. The Second Young Master is one of them, after all.”

Wait, really?

As I blinked at him, Hyuk Mujin launched into an impassioned explanation.

“They’re the greatest young prodigies of the orthodox Murim! The dragons and phoenixes who will lead the Murim of the future! How can you not know about the Ten Dragons and Phoenixes?”

“Hey, hey. Keep your voice down. People are staring.”

He wasn’t exaggerating. Hyuk Mujin’s booming voice had drawn glances from the other customers.

“Who cares if they stare? This is too much even for you, Captain! Are you making fun of me?”

“I don’t know about making fun of people, but I’m good at hitting them.”

“I think I got too worked up. I’m sorry.”

Hyuk Mujin regained his composure in an instant. I turned away from him and gave Cheongpung a friendly smile.

“Please continue.”

“It’s nothing important. I just had a childish thought for a moment.”

Cheongpung looked at me through slightly unfocused eyes. Apparently, he had no intention of using his internal energy to dispel the drunkenness, because he was still a little tipsy.

“Who would be stronger, me or them? I wanted to find the answer to that question.”

In the end, it was because of a martial artist’s competitive pride.

The desire to step into a new world. The desire to defeat a strong opponent and prove his martial arts. I could tell that those feelings had led him down the mountain.

*He seems to have the skill to justify thinking that way, too.*

Jin Mukyung had supposedly reached the Peak realm when he was barely twenty and caused an uproar throughout the Central Plains. Now, he was counted as one of the Ten Dragons and Phoenixes, one of the greatest young prodigies of the orthodox faction.

The Cheongpung in front of me possessed martial talent at least comparable to Jin Mukyung’s.

*He has every right to think so.*

I was nodding inwardly when—

“Puhahaha!”

“Pfft, hahahaha. Ah, holding back my laughter was torture.”

I raised my head toward the source of the sound.

On the second floor, five men and women in silk clothes were looking down at us with faces full of mockery.
```
