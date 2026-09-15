<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0131.txt",
      "sha256": "4cf82f726e0e228c7dc04a34578bee4b58e253a0a06c89471580f3e782f42ec0",
      "bytes": 14032
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9d6eb64593a7ddf654ea79386eed3a2ca842005780e301dcf8088bdbb48f9ecd",
      "bytes": 6862
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "236aa0f96a48d2d33f379016500575ca56a15f8a1d9e8ffda3909efa8f140d69",
      "bytes": 23856
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "667eaad71ebd91bf8aa9a3777108c78da335dd1c2839127597c7a7768eb8d017",
      "bytes": 5199
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "ff83c2e6dafc9a85bc332ef5f27bf3db4fbae83ae9149396e7d53408a5a4b1fa",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "b8ed1aef0e82fcc0c926849871c740f995008ade414891bb06c08e7ba6dc3d6f",
      "bytes": 8154
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "af3a1cea0130113fdd2493cccaad7d17d665dcfb8e30657843d935df5e13d4ce",
      "bytes": 20491
    }
  ],
  "estimated_tokens": 21963
}
-->

# Durable State Update — Chapter 131

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 131. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 131. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 131,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 131,
    "continuity_sources": [131],
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
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle; Wolhwa's real name is Eun Sowol, and she is its Shanxi Branch Leader.",
    "Lee Seowol accepted the Jin Family of Taiyuan's New Year invitation, offered the Mount Heng Sword Sect's territorial rights as an apology, and proposed marriage to Taekyung in exchange for three Peak martial arts; Taekyung plans to reject her because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty; it is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued Mount Heng.",
    "Cheol Mubaek and Lee Cheonbaek became close friends after first meeting and fighting more than thirty years ago; Cheol is the ninth-generation successor of the Shura Annihilating Fist.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; the Fire King and the status of the Fire Gate Clan's single successor remain unknown.",
    "The Temporary Strength Pill is in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers.",
    "The Jin Family of Taiyuan displayed a huge Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night for three days; Wipeng is called the God of Drinking and Taekyung is rumored to be the Night King.",
    "Taekyung's Sleeping Dragon of Shanxi Title effect strengthened to all stats +15 and Fame +200; his current Status Window shows Level 61, Fame 2,100 (+250), and 60 remaining points.",
    "Hyuk Mujin accepted The City Lord's Invitation, requiring attendance at the City Lord's luncheon with young prodigies tomorrow; its reward depends on the City Lord's reaction.",
    "The City Lord of Shanxi Province is a ten-year-old Prince and the Emperor's youngest brother, appointed at age five; Jin Mukyung met him after being summoned three years earlier and considered the encounter a nightmare.",
    "Seokchil is a middle-aged porter with nearly twenty years of experience at the Seongun Escort Bureau in southern Shanxi Province.",
    "Cheongpung is an eccentric young porter hired from Henan for an escort run toward Shanxi; he says he grew up farming and gathering medicinal herbs in the mountains and joined because he did not know the route.",
    "Cheongpung signed a one-year porter contract but paid its fifty-nyang penalty with two silver ingots and gave the excess to Seokchil and the other porter.",
    "Cheongpung recently fled Huashan's Lotus Peak and is traveling toward Taiyuan; he hopes spring will come early and the plum blossoms will bloom profusely."
  ],
  "continuity_sources": [
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
  "safe_through": 130,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, 시진 as shichen, 표행 as escort run, 쟁자수 as porter, 표국 as Escort Bureau, 표두 as Escort Chief, 은원보 as silver ingot, 은자 as nyang of silver, 사서삼경 as the Four Books and Three Classics, and 연화봉 as Lotus Peak.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, 여포 as Lü Bu, 성주의 초청 as The City Lord's Invitation, 친왕 as Prince, 주씨 as Zhu, 천자 as Son of Heaven, 황상 and 황제 as Emperor, 태자 as Crown Prince, 구파일방 as Nine Sects and One Gang, and 오대세가 as Five Great Families."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 기루     | **pleasure house**                               |                                                       |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 129
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; stationed outside Jin Taekyung’s pavilion while Taekyung recovers
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 129
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 129
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

## Korean source

```text
＃131화



“자, 갓 잡은 돼지가 한 근에 스무 푼! 싸다, 싸!”

“어머, 어쩜 좋아. 가락지가 너무 잘 어울린다. 원래 은자 한 냥인데 손가락이 예쁘니까 반 냥. 어때?”

“이 단환으로 말씀드릴 것 같으면, 한 알만 먹어도 정신이 맑아지고 힘이 불끈 솟는…….”

거리는 끝없이 늘어선 가판과 시전 상인들의 쩌렁쩌렁한 외침으로 가득했다.

사람들로 빽빽하게 채워진 태원(太原)의 거리를 본 나는 혀를 내둘렀다.

‘사람 진짜 많네.’

면면도 제법 다양하다. 저잣거리 상인들은 물론, 돌팔이 약장수와 매끄러운 비단옷을 걸친 자도 있고 궁기가 줄줄 흐르는 거지들도 있다.

허리춤에 검을 패용한 무림인들도 심심찮게 보였지만 사람들은 별다른 관심을 보이지 않고 제 할 일을 계속했다.

‘산서성의 성도(成都)라더니.’

산서성에는 수십여 개의 현읍이 존재하지만, 그중에서도 태원이 차지하는 위치는 각별하다.

여러 가지 이점을 가진 덕분에 까마득한 과거엔 어느 왕조(王朝)가 도읍으로 삼았던 적도 있단다.

물론 그 왕조는 멸망한 지 오래지만, 그 후에도 태원은 발전을 거듭해 왔다……고 혁무진한테 들었다.

‘그게 태원진가가 삼백 년을 버틸 수 있었던 이유겠지.’

풍부한 물자와 인력. 그리고 경제력.

생각해 보면 웬 망나니 하나가 가문 공금을 털어 기루에 죄다 쏟아부었는데도 항산검문과 전쟁을 치를 여력은 남아 있었다.

태원진가가 아니라 항산진가였다면 이미 오래전에 쪽박 차고 거리로 나앉았을 거다.



‘태원진가의 땅을 밟지 않고서는 태원을 지나갈 수 없다.’



언젠가 들었던 말을 떠올리는 내게 혁무진이 물었다.

“무슨 생각을 그렇게 하세요?”

“땅 투기가 좋긴 좋구나. 뭐 그런 생각.”

“예?”

“그런 게 있어. 넌…….”

“몰라도 된다고요?”

“잘 아네.”

“그 말도 이제 지겹습니다.”

“그래, 나도 너 지겹다.”

“그럼 절 왜 데려오셨습니까?”

“입은 비뚤어져도 말은 바로 하자. 내가 데려온 게 아니라 큰형님이 붙여 준 거야.”

진위경은 내일 있을 산서 성주와의 오찬에 대비해 나를 먼저 보냈다. 아무래도 변덕이 심한 어린아이니 별다른 잡음 없이 최대한 맞춰 주려는 의도 같다.

아무튼, 그 때문에 혁무진이 나와 동행했다. 태원 토박이인 녀석은 여러모로 수행원으로서 안성맞춤이었다.

“그러고 보니까 여기가 네 고향 아니냐?”

“고향이라, 그렇죠.”

혁무진이 복잡한 눈빛으로 거리를 응시했다.

“고작 오 년밖에 안 지났는데…… 참 많이 바뀌었네요.”

“중간중간 몇 번은 들렀을 것 아냐.”

“아뇨. 그동안 한 번도 안 들렀는데요.”

뜻밖의 이야기에 깜짝 놀랐다.

“오 년 동안 단 한 번도?”

“제가 무공을 좀 늦게 시작했거든요. 다른 사람들을 따라잡으려면 별수 있겠습니까. 열 배, 스무 배로 노력하는 수밖에요.”

“으음.”

“이렇게 돌아올 줄은 몰랐습니다.”

오랜만에 아니, 거의 처음 보는 진지한 모습이다.

생각해 보면 혁무진 이 녀석은 매사에 실없이 굴어도 나름 한가락 하는 일류 고수였다. 워낙 주위에 괴물들이 득실거려서 그렇지, 결코 낮은 경지가 아니다.

그만큼 피나는 노력이 뒷받침되었기에 가능한 일이었겠지. 거기에 더해서…….

‘재능도 있는 편인 것 같고.’



[Lv.48 혁무진]



빠른 속도로 쑥쑥 올라가는 레벨이 그 증거다.

이 녀석, 이러다가 갑자기 절정 고수라도 되는 거 아냐?

내 새삼스러운 시선에도 오랜만에 고향을 방문한 혁무진은 감상에 젖어 있기 바빴다.

“아, 저 아주머니 아직도 계시네.”

반가우면서도 아련한 목소리다.

혁무진이 손을 들어 가리킨 곳에는 머리가 희끗희끗한 중년 여인이 작은 좌판 앞에서 각종 군것질거리를 팔고 있었다.

“혹시 빙당호로(冰糖葫芦) 좋아하세요?”

평소였으면 헛소리 그만하고 갈 길이나 가자고 했겠지만 어째 분위기가 심상찮다. 나는 최대한 친절하게 대꾸했다.

“태어나서 한 번도 안 먹어 봤어.”

“어릴 때는 빙당호로가 그렇게 먹고 싶더라고요. 좌판 앞에 쭈그려 앉아서 손가락만 빨고 있으면 아주머니께서 한두 개씩 쥐여 주셨죠.”

혁무진이 씁쓸하게 웃으며 말을 이었다.

“그럴 때마다 다른 아이들이 얼마나 부러웠는지 모릅니다. 하나같이 부모님 손을 꼭 잡고 와서 빙당호로며 당과를 사서 저잣거리를 돌아다니던 그 모습…… 아직도 눈에 선해요.”

이 분위기를 어떻게 해야 하나.

어느 정도 사연이 있을 거라고는 생각했지만 이야기가 이렇게 흘러갈 거라고는 예상치 못했다.

‘오 년 만에 왔다는 것부터 눈치챘어야 했는데.’

이곳, 무림에는 유난히 고아가 많다. 당장 주변만 둘러봐도 저잣거리에 꾀죄죄한 누더기를 걸치고 돌아다니는 어린아이들을 쉽게 발견할 수 있으니까.

‘아마 녀석도 비슷한 처지였겠지.’

가족이 없으니 돌아올 이유도 없다. 와 봐야 빙당호로가 먹고 싶어 좌판 앞을 서성이던 어린 시절의 아픈 기억만 떠오를 뿐이다.

그래서 수련으로 그 아픔을 잊으려 한 것일지도 모른다.

녀석에게는 태원진가가 집이고 동료들이 가족이었던 거다.

‘그것도 모르고…… 내가 그동안 너무 함부로 대했어.’

젠장, 괜히 코끝이 찡해진다.

이런 내 변화를 혁무진은 금방 알아차렸다.

“왜 그러세요?”

“아니, 그냥. 오늘 미세먼지가 심해서 그런가, 코가 간질간질하네.”

“미세먼지요?”

“그건 넘어가고, 빙당호로나 하나씩 먹을까?”

“객잔부터 미리 들르는 게 좋을 것 같은데요. 해 떨어지기 전에 객실을 잡아 놓지 않으면 자리가 없어서.”

“야, 저거 하나 먹는 데 뭐 얼마나 걸린다고 그래. 그렇게 비싼 것도 아니고. 어차피 경비도 넉넉하게 받았을 거 아냐?”

“그건 그렇죠.”

“이참에 먹고 싶은 거 다 먹고 실컷 놀다 가자. 너 어렸을 때 저 아주머니한테 얻어먹은 것도 갚을 겸 매상 잔뜩 올려 드려.”

“필요한 곳에 쓰라고 주신 경비를 이렇게 써도 될지…….”

“써, 다 써. 나중에 뭐라 하는 놈 있으면 나한테 데려와.”

“이공자님이 뭐라고 하시면요?”

“……그 인간은 빼고 데려와.”

혁무진이 피식 웃더니 한층 밝아진 목소리로 말했다.

“그럼 빙당호로나 하나씩 먹을까요?”

“그래, 아까부터 보고 있으니까 침 고인다.”

다분하게 혁무진을 의식한 말이다. 내일모레면 서른인데 과일 사탕 따위에 침이 고이긴 무슨.

‘이렇게라도 기분이 좋아지면 된 거지.’

저 녀석도 그동안 나 따라다니느라 고생 많았다. 틈만 나면 구박받고, 얻어맞고, 퀘스트만 했다 하면 괴물 같은 놈들만 만나는 바람에 죽을 고비도 여러 번 넘겼다.

혁무진과의 첫 만남은 분명 악연이었지만 이제는 아니다.

“야, 무진아.”

막 좌판을 향해 걸어가려던 혁무진이 멈칫했다.

“예? 왜요?”

“그…….”

앞으로도 잘 부탁한다는 말이 혀끝에서 맴돈다. 젠장, 시커먼 두 사내놈이 주고받기에는 너무 간질거리는 말이다.

고민 끝에 결국 엉뚱한 소리만 툭 튀어나왔다.

“각자 두 개씩 먹자. 큰 걸로.”

“아, 예.”

괜히 부끄러워서 먼 산을 바라보는 내 귓가로 혁무진과 중년 여인의 대화가 흘러들어 왔다.

“어머! 너 무진이 아니니? 혁무진. 맞지?”

“오랜만에 뵙습니다. 아주머니.”

“세상에, 맞네. 맞아. 하마터면 못 알아볼 뻔했다, 얘.”

“아주머니는 여전하신데요.”

“호호호, 말이라도 고맙네. 무진이 너는 잘 지내고? 듣기로는 무인이 됐다던데.”

“예. 태원진가 소속입니다. 곧 수문각주로 승진해요.”

“태, 태원진가? 수문각주? 세상에, 세상에…….”

수문각주로 승진할지 말지는 두고 봐야 알겠지만 절로 흐뭇한 미소가 지어지는 대화다.

‘무슨 라디오 사연 같네.’

늘 주위를 맴도는 고아 아이에게 빙당호로를 건네주곤 했던 맘씨 좋은 아주머니. 곤궁했던 어린 시절을 보낸 아이는 피나는 노력 끝에 마침내 성공하여 훌쩍 장성한 모습으로 돌아와 재회한다.

어디선가 한 번쯤 들어 본 이야기지만 감동적이라는 사실은 변함이 없다.

“크흠, 이거 참, 눈에 뭐가 들어갔나…….”

이건 황사인가 미세먼지인가. 아직 공장은 안 세웠을 테니 황사겠지.

나도 모르게 눈시울이 살짝 붉어진 그 순간이었다.

“그래, 부모님은 찾아뵈었고?”

“아직요. 오늘이나 내일쯤에 한 번 들러볼 생각입니다.”

“빨리 가 봐라. 너희 집 이사 간 건 아니?”

“이사요? 어디로요?”

“저쪽 대로변에 큰 장원으로 갔다. 연못에 비단잉어도 풀어 놓고 키우더라.”

“아, 그래요?”

“……?”

부모님? 이사? 커다란 장원에 비단잉어?

잠깐. 이거 뭔가 이상한데. 황당해진 나는 빙당호로를 들고 돌아오는 혁무진에게 물었다.

“무슨 소리야?”

“예? 뭐가요?”

“너희 부모님 살아 계셔?”

혁무진이 나를 미친놈처럼 바라보았다.

“멀쩡한 부모님을 왜 죽입니까?”

“아니 그게 아니고…… 그럼 아까 했던 말은 뭔데.”

“무슨 말이요?”

“빙당호로. 그거 못 먹어서 맨날 손가락 쪽쪽 빨았다며?”

“못 먹었죠. 부모님이 이빨 썩는다고 못 먹게 했어요. 여기 상인분들이야 저희 부모님 성격 극성인 거 다 아니까 일부러 저한테만 안 팔았는데, 저분만 몰래 하나씩 챙겨 주셨고.”

“……부모님 손 잡고 다니는 애들 부러웠다는 건?”

“저희 집 장사가 워낙 잘돼서 시간이 안 나시더라고요. 혼자 놀았죠, 뭐.”

“그, 그럼 태원에 가족이 있으면서 오 년 동안 한 번도 안 왔다고?”

“집 나왔어요. 가업 물려받기 싫어서 편지 한 통 남기고. 본가 수문각주님이 저희 아버지 불알친구라 제 근황은 다 알고 계셨을 겁니다.”

“…….”

“한 이 년 동안은 엄청 뭐라 하셨는데, 갑자기 막둥이가 태어나서 제가 가업을 이을 필요가 없어지니까 그 후부터는 별말씀 안 하시던데요?”

목을 길게 빼고 두리번거리던 혁무진이 손을 들어 뭔가를 가리켰다.

“아, 저기 있다. 보이시죠? 저 건물이 저희 부모님 건데…… 저 없는 동안 더 커졌네요.”

나는 혁무진의 손가락을 따라 고개를 돌렸다.

우뚝 솟은 거대한 5층짜리 전각과 커다란 글씨로 쓰인 현판이 눈에 들어온다.



[혁가 포목점]



혁무진은 뿌듯하게 웃었다.

“태원에서 가장 큰 포목점입니다. 하남과 하북에 지점도 있어요.”

이 새끼도 금수저구나…….

이렇게 살벌한 동네에서 체인점까지 낼 정도면 말 다 했다.

‘내가 뭘 한 거냐.’

빙당호로가 먹고 싶어서 손가락 쪽쪽 빨던 어린 소년?

실상은 성공한 사업가 부모님이 아들놈 치아 건강을 생각해서 못 먹게 한 거였다.

‘아니 시벌, 이게 무슨.’

입만 벌린 채 서 있는 내게 혁무진이 손에 든 빙당호로를 건넸다.

“자, 하나 드세요. 제가 특별히 가장 크고 영롱한 걸로 골랐습니다. 이 근방에서는 저분이 파시는 빙당호로가 최고예요.”

“이런 호로색…….”

목구멍까지 솟구치는 욕을 꿀꺽 삼키고 빙당호로를 까드득 깨물었다.

“이제 빨리 객실이나 잡으러 가자.”

“벌써요? 이제 겨우 철전 몇 푼 썼는데…….”

“마! 그게 네 돈이야? 필요할 때 쓰라고 준 경비잖아, 경비!”

“아니, 방금은 실컷 쓰고 놀다 가자면서요?”

“이 정도면 놀 만큼 놀았어. 해 떨어지면 객실 찬다며. 오늘 잠자리가 뒤숭숭해서 내일 오찬에 늦으면 네가 책임질래?”

“…….”



* * *



홍화객잔.

현판에 적힌 객잔 이름에서 알 수 있듯 이곳은 하오문의 손이 뻗친 곳 중 하나였다.

‘밤에는 홍화루. 숙박은 홍화객잔이라.’

거, 누구 생각인지 취객들 등골까지 뽑아 먹으려고 작정을 했구먼.

“들어가자.”

아까부터 주둥이가 댓 발 나온 혁무진을 데리고 객잔 입구를 향해 다가가려던 그때였다.

“저어, 죄송합니다만.”

그건 묘하게 신경을 잡아당기는 목소리였다. 꿈꾸는 듯 몽롱하고, 어린아이처럼 천진난만한 목소리의 주인은 서글서글한 인상의 청년이었다.

‘이 느낌은…….’

돌아서서 그의 맑은 눈동자를 마주 본 순간, 나도 모르게 숨이 막혔다.

그건 진무경과는 다른 종류의 기세였다.



[Lv.??? 청풍]



또 다른 절정 고수의 등장. 긴장감 속에서 청년, 청풍의 입술이 열렸다.

“실례가 안 된다면 빙당호로 하나만 먹어도 되겠습니까?”

“……?”

이건 또 뭐 하는 새끼냐.
```

## Final English reading copy

```markdown
# Chapter 131

“Fresh-killed pork, twenty coins per geun! Cheap, cheap!”

“Oh my, what should I do? That ring suits you perfectly. It’s normally one nyang of silver, but you have such pretty fingers, so I’ll give it to you for half a nyang. What do you say?”

“If I may say so, this pill will clear your mind and fill you with strength after just one dose…”

The streets were filled with endless rows of stalls and the booming cries of market merchants.

When I saw the crowded streets of Taiyuan, I clicked my tongue in amazement.

*There are a hell of a lot of people.*

There was quite a variety among them, too. There were not only street vendors, but also quack medicine sellers, people dressed in smooth silk, and beggars whose poverty practically poured off them.

Martial artists wearing swords at their waists were easy enough to spot, but no one paid them any particular attention. Everyone simply continued with whatever they were doing.

*So this is the capital of Shanxi Province.*

Shanxi Province had dozens of counties and towns, but Taiyuan held a particularly important position among them.

Thanks to its many advantages, it had once served as the capital of a dynasty in the distant past.

That dynasty had fallen long ago, of course, but Taiyuan had continued to develop afterward…

At least, that was what Hyuk Mujin had told me.

*That must be why the Jin Family of Taiyuan has managed to survive for three hundred years.*

Abundant supplies and manpower. And economic power.

Come to think of it, even after some worthless son had plundered the family treasury and dumped all of it into a pleasure house, they had still possessed enough strength to go to war with the Mount Heng Sword Sect.

If they had been the Jin Family of Mount Heng instead of the Jin Family of Taiyuan, they would have gone bankrupt and ended up on the streets long ago.

*You can’t pass through Taiyuan without setting foot on the Jin Family of Taiyuan’s land.*

As I recalled something I had heard long ago, Hyuk Mujin asked,

“What are you thinking about so seriously?”

“Land speculation is pretty great. That’s what I was thinking.”

“What?”

“It’s nothing. You…”

“I don’t need to know?”

“You catch on quickly.”

“I’m getting tired of hearing that.”

“Yeah, I’m getting tired of you, too.”

“Then why did you bring me along?”

“Let’s at least get the facts straight. I didn’t bring you. The eldest brother assigned you to me.”

Jin Wikyung had sent me ahead in preparation for tomorrow’s luncheon with Shanxi’s City Lord. I assumed he wanted to accommodate the capricious child as much as possible without causing any trouble.

In any case, that was why Hyuk Mujin was traveling with me. As a native of Taiyuan, he was an ideal attendant in many ways.

“Come to think of it, isn’t this your hometown?”

“My hometown… Yes, it is.”

Hyuk Mujin stared at the streets with complicated emotions in his eyes.

“It’s only been five years, but so much has changed.”

“You must have stopped by a few times in between.”

“No. I haven’t visited even once during that time.”

I was startled by the unexpected answer.

“Not even once in five years?”

“I started learning martial arts rather late. If I wanted to catch up with everyone else, I had no choice but to work ten or twenty times harder.”

“Hmm.”

“I never thought I’d return like this.”

It was the first time in a long while—no, almost the first time ever—that I had seen him look so serious.

Come to think of it, Hyuk Mujin was a First Rate master who had quite a bit of skill, even though he acted foolishly about everything. It was just that he happened to be surrounded by monsters. His realm was by no means low.

He could only have reached that level through tremendous effort. And on top of that…

*He seems to have some talent, too.*

> **System**
>
> **Level:** 48  
> **Name:** Hyuk Mujin

The rapidly rising Level was proof of that.

*Is this guy going to suddenly become a Peak master one of these days?*

Despite my newly appreciative gaze, Hyuk Mujin was too absorbed in the emotions of returning to his hometown after so long.

“Ah, that auntie is still here.”

His voice was happy, yet wistful.

The middle-aged woman he pointed toward had streaks of gray in her hair and was selling various snacks from a small stall.

“Do you like candied hawthorn skewers?”[^1]

Under normal circumstances, I would have told him to stop talking nonsense and keep moving, but the atmosphere was unusual. I answered as kindly as possible.

“I’ve never eaten one in my life.”

“When I was young, I wanted one so badly. Whenever I crouched in front of the stall and sucked on my fingers, that auntie would give me one or two.”

Hyuk Mujin continued with a bitter smile.

“You have no idea how envious I was of the other children. They would come holding tightly to their parents’ hands, buy candied hawthorn and sweets, and walk around the market… I can still see it clearly.”

What was I supposed to do with this atmosphere?

I had assumed there would be some sort of story behind him, but I hadn’t expected it to go in this direction.

*I should have realized something when he said he hadn’t come back for five years.*

There were an unusually large number of orphans in the Murim. Even looking around us, it was easy to find children wandering through the market in filthy rags.

*He must have been in a similar situation.*

If he had no family, he had no reason to return. Coming back would only remind him of the painful memories of standing around the stall as a child, wanting to eat candied hawthorn.

Maybe that was why he had tried to forget his pain through training.

For him, the Jin Family of Taiyuan had been home, and his companions had been his family.

*And without knowing any of that… I’ve been treating him far too harshly.*

Damn it. The tip of my nose was starting to sting for no reason.

Hyuk Mujin immediately noticed the change in me.

“What’s wrong?”

“No, it’s nothing. Maybe the fine dust is especially bad today. My nose feels itchy.”

“Fine dust?”

“Forget that. Why don’t we each get a candied hawthorn skewer?”

“Wouldn’t it be better to find an inn first? If we don’t get a room before the sun goes down, there may not be any left.”

“Hey, how long does it take to eat one of those? They’re not even that expensive. We were given plenty of travel expenses, weren’t we?”

“That’s true.”

“Let’s eat whatever we want and have as much fun as we can before we leave. You can raise that auntie’s sales while paying her back for all the candied hawthorn she gave you when you were young.”

“I’m not sure it’s right to spend the money we were given for things we need on this…”

“Spend it. Spend every bit of it. If anyone complains later, bring them to me.”

“What if the Second Young Master complains?”

“...Bring anyone but him.”

Hyuk Mujin let out a short laugh before speaking in a much brighter voice.

“Then shall we each get a candied hawthorn skewer?”

“Sure. I’ve been looking at them for a while, and they’re making my mouth water.”

I was saying that very deliberately for Hyuk Mujin’s sake. I was almost thirty. What kind of adult salivated over fruit candy?

*As long as it makes him feel better.*

That guy had suffered plenty while following me around. He was constantly berated and beaten, and every time we took on a Quest, we ended up meeting nothing but monsters. He had come close to dying more than once.

My first meeting with Hyuk Mujin had certainly been an ill-fated one, but that was no longer true.

“Hey, Mujin.”

Hyuk Mujin, who had just started walking toward the stall, stopped short.

“Yes? What is it?”

“That…”

The words *I’m counting on you from here on out* hovered at the tip of my tongue. Damn it. That was far too embarrassing for two grown men to say to each other.

After agonizing over it, I ended up blurting out something completely different.

“Let’s each have two. The big ones.”

“Oh. Yes.”

Too embarrassed to look at him, I stared off at a distant mountain. That was when I heard Hyuk Mujin speaking with the middle-aged woman.

“Oh my! Aren’t you Mujin? Hyuk Mujin, right?”

“It’s been a long time, Auntie.”

“My goodness, it is you. It is! I almost didn’t recognize you, child.”

“You haven’t changed at all, Auntie.”

“Ho-ho-ho. That’s kind of you to say. Have you been well, Mujin? I heard you became a martial artist.”

“Yes. I belong to the Jin Family of Taiyuan. I’ll be promoted to Master of the Gatekeeper Pavilion soon.”

“T-Taiyuan Jin Family? Master of the Gatekeeper Pavilion? My goodness, my goodness…”

Whether he would actually be promoted to Master of the Gatekeeper Pavilion remained to be seen, but the conversation brought a pleased smile to my face.

*This sounds like a radio call-in story.*

A kindhearted auntie who used to give candied hawthorn to the orphan child who was always lingering around her stall. After years of backbreaking effort, the child who had endured a difficult childhood finally succeeded and returned as a tall, grown man.

It was a story I had heard somewhere before, but that didn’t make it any less moving.

“Ahem. What is this? Did something get in my eye?”

Was this the yellow dust or the fine dust? Factories couldn’t have been built yet, so it must have been yellow dust.

That was when the rims of my eyes reddened slightly despite myself.

“So, have you gone to see your parents?”

“Not yet. I was thinking of stopping by today or tomorrow.”

“Go see them soon. Didn’t your family move?”

“Move? Where did they go?”

“They moved into a large estate along the main road over there. They even released koi into the pond and raised them.”

“Oh, really?”

“...?”

Parents? Moving? A huge estate with koi?

Wait. Something was wrong here. I asked Hyuk Mujin, who was returning with the candied hawthorn skewers in his hands.

“What were you talking about?”

“Huh? About what?”

“Are your parents still alive?”

Hyuk Mujin stared at me as though I were insane.

“Why would I kill my perfectly healthy parents?”

“No, that’s not what I meant… Then what were you talking about earlier?”

“What did I say?”

“About the candied hawthorn. You said you couldn’t eat it and spent every day sucking your fingers.”

“I couldn’t eat it. My parents wouldn’t let me because they said it would rot my teeth. All the merchants around here knew how overbearing my parents were, so they made a point of refusing to sell any to me specifically. That lady was the only one who would secretly slip me one.”

“…”

“And what about being jealous of the children who walked around holding their parents’ hands?”

“My family’s business was so successful that they never had any free time. I played by myself.”

“Th-then you had family in Taiyuan, and you didn’t visit even once in five years?”

“I left home. I didn’t want to inherit the family business, so I left a single letter behind and ran away. The Master of the Gatekeeper Pavilion in our family is my father’s childhood best friend, so he probably knew everything about how I was doing.”

“…”

“For about two years, they gave me hell over it. Then my youngest sibling was suddenly born, so I no longer needed to inherit the family business. After that, they stopped saying much.”

Hyuk Mujin stretched his neck and looked around before raising a hand to point at something.

“Ah, there it is. Do you see it? That building belongs to my parents… It got even bigger while I was gone.”

I followed Hyuk Mujin’s finger and turned my head.

A huge, towering five-story pavilion and a signboard bearing enormous characters came into view.

**Hyuk Family Textile Shop**

Hyuk Mujin smiled proudly.

“It’s the largest textile shop in Taiyuan. We have branches in Henan and Hebei, too.”

*This bastard is a rich kid, too…*

You had to be pretty damn wealthy to open chain stores in a place this rough.

*What the hell have I been doing?*

A young boy who used to suck on his fingers because he wanted to eat candied hawthorn so badly?

In reality, his successful business-owner parents had forbidden him from eating it because they were worried about their son’s dental health.

*What the fuck is this?*

As I stood there with my mouth hanging open, Hyuk Mujin held out one of the candied hawthorn skewers.

“Here, have one. I specially chose the biggest and shiniest one. The ones that lady sells are the best in this area.”

“You son of a…”

I swallowed the curse that had surged up to my throat and bit down on the candied hawthorn with a loud crunch.

“Let’s hurry up and find a room.”

“Already? We’ve only spent a few copper coins…”

“Hey! Is it your money? It’s travel expenses they gave us to use when necessary. Expenses!”

“Didn’t you just say we should spend it all and have fun?”

“We’ve had enough fun. You said the rooms would fill up after sunset. If we get a bad night’s sleep and end up late to tomorrow’s luncheon, are you going to take responsibility?”

“…”

* * *

Honghwa Inn.

As could be guessed from the name written on its signboard, this was one of the places under the Lower District Sect’s influence.

*Honghwaru at night. Honghwa Inn for lodging.*

Whoever had come up with that arrangement had clearly intended to wring every last penny from drunken customers.

“Let’s go in.”

I was about to lead Hyuk Mujin, who had been pouting since earlier, toward the inn’s entrance when someone spoke.

“Excuse me, I’m sorry to bother you.”

The voice strangely tugged at my nerves. Its owner was a young man with an affable expression and a dreamy, hazy voice as innocent as a child’s.

*This feeling…*

The moment I turned around and met his clear eyes, I found it difficult to breathe.

This was an aura different from Jin Mukyung’s.

> **System**
>
> **Level:** ???  
> **Name:** Cheongpung

Another Peak master had appeared.

Amid the tension, the young man named Cheongpung opened his lips.

“If you don’t mind, may I eat just one candied hawthorn skewer?”

“...?”

*What the hell is this guy?*

[^1]: Candied hawthorn skewers are a traditional snack made by coating skewered fruit in hardened sugar.
```
