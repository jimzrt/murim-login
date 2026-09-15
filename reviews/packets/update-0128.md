<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0128.txt",
      "sha256": "d0b5787a9286b55969f2a96d2ba18337045e9bf68c2c5817321c6bceec1c59f0",
      "bytes": 13937
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d72d53533b0b000c98a7e31e46c137681d2804a3c4aad559b149835b5fb6c515",
      "bytes": 6229
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d679d5c2110c57a08d37406a2e77650daf2d31b078aabdff2a54e0268b44401d",
      "bytes": 22427
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "49fdf8bbfc57c033e8e93973327547a8cbf7bd8472b9c5711b017696177c06c2",
      "bytes": 5199
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "1b1e362976452d4177018618273b8323a2ec99e7448a622f5f064a24ad5de48e",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b7c8a6a35e09fe8ba10843962876e2c901f0b1a9f5b8e13bd5561c316339e547",
      "bytes": 24450
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "c89f13f948b14fa9c98fb5807c3165eaa0bad6c480ec18da0cf1f05405162a15",
      "bytes": 8154
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "a392a48ae3401ef8b15f94304b37e844701ac099bb783ae9474ec102b9fbf3ea",
      "bytes": 1356
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "50dd727159f9307eceefb2341207f9796121e0567795ee21f784969396d51112",
      "bytes": 4621
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "ef417c895a3999bc0f87d77256526790c62032fa1d4d18a9cb139fd3ea54787c",
      "bytes": 2374
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "badd58dcf30ec91f3e4cdb1d85fa9dcf4c034b16c7e83f316c248cd44618ccf0",
      "bytes": 18945
    }
  ],
  "estimated_tokens": 22263
}
-->

# Durable State Update — Chapter 128

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 128. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 128. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 128,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 128,
    "continuity_sources": [128],
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
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered; his chest wound reopened during the drinking gathering and was treated by a physician.",
    "Cheol Mubaek remains severely injured and needs extended recuperation; he is the ninth-generation successor of the Shura Annihilating Fist and protector of Lee Seowol.",
    "Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect and vows to preserve it for those who died defending it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering and offered the Mount Heng Sword Sect's territorial rights to the Jin Family as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; Taekyung has decided to reject the proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine.",
    "The Lower District Sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued the Mount Heng Sword Sect.",
    "Cheol Mubaek and Lee Cheonbaek first met more than thirty years ago, fought, and became close friends; the Shura Annihilating Fist was an ancient top-ten fist technique whose lineage was believed to have ended and is no longer current among the top ten.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; Taekyung possesses its manual, a Fire Gate Clan secret restricted to owners of Scorching Yang Qi.",
    "The Fire King is a Supreme Peak master among the world's twenty greatest experts; his current status is unknown, and the Fire Gate Clan has a single successor.",
    "The Mount Heng Sword Sect formally apologized for Lee Cheonbaek's crimes, but Taekyung refused the apology and directed responsibility toward the Jin Family of Taiyuan.",
    "The Temporary Strength Pill is stored in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its updated System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, following price, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers; Wikyung was told that Pung Yang had died, the Red Wind Band had been annihilated, Taekyung had defeated Pung Yang, and Mukyung had suffered severe but nonfatal injuries.",
    "The Jin Family of Taiyuan displayed a huge Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night; Wipeng is called the God of Drinking, Taekyung is rumored to be the Night King, and the System raised Taekyung's Fame by 20, 22, and 25."
  ],
  "continuity_sources": [
    127
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Was Jopil truly the nineteenth-generation successor of the Flame Divine Palm, and how did he acquire it?",
    "Who called out to Jin Mukyung and Jin Taekyung from the distance at the chapter's end?"
  ],
  "safe_through": 127,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, and 시진 as shichen.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, and 천하십대권법 as the ten greatest fist techniques in the world.",
    "Render 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, and 화북 as North China."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 127
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; stationed outside Jin Taekyung’s pavilion while Taekyung recovers
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 127
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 126
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 127
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 127
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 127
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 124
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃128화



장 노인은 시끄러운 소리에 잠에서 깼다.

‘어느 육시랄 놈들이.’

가뜩이나 늙어서 점점 잠이 줄어드는 그로서는 달갑지 않은 상황이었다.

‘어떤 놈들인지 면상이나 한번 보자.’

뻐근한 몸을 이끌고 초가집을 나선 장 노인이 가장 먼저 발견한 것은 구름처럼 모여 있는 인파였다.

그 숫자가 어림잡아 수백. 마을 안에 발 달린 것들은 사람이고 짐승이고 죄다 모여 있는 것 같았다.

“이게 다 뭔 일이여?”

워낙 고만고만한 마을이다 보니 대부분 아는 얼굴이다.

장 노인의 중얼거림에 익숙한 얼굴의 시전 상인이 알은체를 했다.

“일어나셨습니까.”

“이렇게 난리를 쳐 대는데 안 일어나고 배겨?”

“하하, 어르신께서 이해하십시오. 귀한 손님이 오신다는 말에 다들 모여 있는 거니까요.”

장 노인이 퉁명스럽게 대꾸했다.

“귀한 손님? 황상(皇上)이라도 오나?”

“아이고, 또 그러신다. 황상께서 어르신 친굽니까?”

“나이로 따지면 내가 애비지.”

“그러다가 역모죄로 잡혀갑니다. 저기 관군들 안 보이세요?”

“관군?”

상인의 턱짓에 수십 명의 관군과 관복을 차려입은 현령(懸令)을 발견한 장 노인이 눈을 가늘게 떴다.

“마적 놈들 어슬렁거릴 때는 보이지도 않던 놈이 관복까지 차려입어? 그 귀한 손님이 고관대작이라도 되나?”

“고관대작은 아니지만 산서성에서는 이겁니다, 이거.”

상인이 엄지를 치켜세운 그 순간, 몰려 있던 사람들의 입에서 탄성이 터져 나왔다.

“저기 온다!”

“왔다!”

장 노인은 사람들의 시선을 따라 고개를 돌렸다. 멀리서부터 달려오는 오십 기의 기마와 휘날리는 깃발을 확인한 그는 그제야 귀한 손님의 정체를 알 수 있었다.

‘태원진가.’

세상 돌아가는 일에는 별 관심이 없는 장 노인이었지만 태원진가의 이름만은 귀가 닳도록 들었다.

장장 삼백 년간 명맥을 이어 온 명가(名家)이자 산서성의 패권을 틀어쥔 패자(霸者).

위풍당당한 행렬을 지켜보던 장 노인이 문득 미간을 좁혔다.

‘그놈이 누구였더라. 그, 뭐냐. 산서, 산서…… 무슨 용이었는데?’

나이를 먹으니 기억력도 떨어진다. 지나간 세월에 야속함을 느끼던 장 노인의 눈에 한 사람이 들어왔다.

“여보게, 저 젊은이가 누군가?”

“아, 저 소협 말입니까?”

당장 보이는 태원진가의 무인만 자그마치 수십 명이다. 그러나 상인은 대번에 알아들었다.

낭중지추. 젊은이의 존재는 주머니 속의 송곳과 같아서 어디에서나 눈에 띄니 이상한 일도 아니다.

“산서잠룡입니다.”

스릉-

마치 그 말을 들은 것처럼, 선두에 선 청년이 허리춤에 찬 검을 뽑아 들었다.

투명한 검신이 햇빛을 받아 번쩍 빛남과 동시에 거대한 함성이 터져 나왔다.

“와아아아아!”

“태원진가! 산서잠룡! 진천검!”



* * *



“산서잠룡! 진태경! 산서잠룡! 진태경!”

사방에서 울려 퍼지는 내 별호와 이름. 지난 며칠간 이미 몇 번을 겪었음에도 뿌듯하다.

‘아이돌이 이런 기분인가.’

저거 그거잖아. 우윳빛깔 진태경. 사랑해요. 진태경.

음악 예능에서나 보던 아이돌 팬클럽이 눈앞에 있다. 나는 흐뭇하게 웃으며 허리춤에 찬 [이름 없는 검]을 뽑아 들었다.

스르릉. 번쩍!

브랜드가 만년한철이라 그런지 시각 효과로는 이만한 게 없더라.

“우와아아아아!”

“꺄아악! 공자님 절 가져요!”

“응애! 응애!”

남녀노소, 전 연령대를 아우르는 전체 이용가 같은 남자.

그게 바로 나다.

띠링.



- 명성이 19 상승합니다!

- 명성이 26 상승합니다!

- 명성이 31 상승합니다!

.

..

- 명성이 대폭 상승합니다!

- 명성의 증가로 칭호, [산서잠룡]의 효과가 강화됩니다!



‘칭호 효과가 강화됐다고?’

생각지도 못한 수확이다. 변경된 내용도 확인해 볼 겸, 상태창을 켰다.

띠링.



상태창



[Lv.61 진태경]

직업 : 일류 무인

명성 : 2100 (+250)

칭호 : 4개 (칭호 효과 적용 중)

- 귀환자 (모든 능력치 +10)

- 산서잠룡 (모든 능력치 +15, 명성 +200)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

근력 : 196 (+30)체력 : 195 (+30)

민첩 : 192 (+30)지력 : 35(+30)

매력 : 35 (+30)공력 : 45년

맷집 : 155 (+30)

잔여 포인트 : 60

- 잔여 포인트를 분배하십시오.





모든 능력치 10, 명성 100 상승이었던 산서잠룡의 칭호 효과가 확실히 변했다.

‘이름값이 높아졌다, 이건가?’

칭호라는 건 하늘에서 뚝 떨어지는 게 아니다.

나만 해도 잠룡이니 뭐니 하는 소문이 슬금슬금 퍼지더니 어느 순간 명성이 오르면서 산서잠룡이라는 칭호를 얻게 됐다.

아마 명성이 높아질수록 칭호 효과도 상승하는 듯싶었다.

‘레벨도 벌써 60이 넘었고.’

오랜만에 확인한 상태창은 쑥쑥 커 있었다. 훌쩍 솟구친 명성과 200에 가까워진 전투 능력치. 45년의 빵빵한 공력까지.

‘크으으. 주모!’

짜릿함에 몸을 부르르 떨자 오른편에서 깃발을 들고 있던 혁무진이 나를 정신병자 보듯 바라봤다.

“그렇게 좋으십니까?”

나는 짐짓 정색하며 대답했다.

“누가 좋아했다고 그래. 그냥 사람들이 좋아하니까 분위기 좀 띄워 준 거지.”

“……할 말은 많지만 하지 않겠습니다.”

“현명한 선택이야.”

사람들의 환호 속에서 걷던 우리는 말고삐를 당겨 속도를 늦췄다.

우르르 쏟아져 나와 앞길을 가로막은 수십 명의 사내 때문이었다.

그 가운데 혼자 화려한 붉은색 옷을 차려입은 뚱뚱이가 나를 보고 활짝 웃었다.

“허허, 듣던 대로 헌앙하시구려. 산서잠룡의 위명은 내 익히 들었소이다.”

“아, 예.”

나는 어리둥절해져서 물었다.

“그런데 누구세요?”

혁무진이 황급히 속삭였다.

“현령이잖아요, 현령.”

“현령이 뭔데.”

“네? 현령이 뭔지도 모르세요?”

“이장 같은 건가?”

“와, 미치겠네. 그냥 벼슬아치라고 생각하세요.”

“아, 벼슬아치. 그럼 뒤에 있는 사람들이 관군?”

“……왜 이러세요, 관군 처음 보는 사람처럼.”

“아니, 그냥 신기해서.”

사실 진짜 처음 본다.

나는 유심히 뚱뚱이, 아니 현령과 그 부하들을 살펴봤다.

이 세상에도 나라가 있고 관아나 법 집행 기관이 있다는 사실은 알았지만 이렇게 실제로 마주친 건 처음이다.

‘어떻게 코빼기도 안 비출 수가 있냐.’

하루에도 수십 건씩 강력 범죄가 일어나는 동네인데 관군들이 범인 잡아가는 건 구경도 못 해 봤다.

하기야, 약 2천 명이 맞붙었던 팔천협 전투나 이번 적풍단 관련해서도 아무런 제재가 없었던 걸 생각해 보면 그 정도는 당연한 건가.

‘그렇다고 어슬렁거리는 마적 놈들 때려잡는 것도 아니고.’

이 자식들은 하는 일이 뭘까?

현대였다면 무림인 중 절반은 살인죄로 교도소 독방에 갇혀 있을 거라는 상상을 할 때였다.

“커흠, 커흐흠!”

현령이 벌겋게 달아오른 얼굴로 헛기침을 했다.

저 양반도 나름 직위가 있는 벼슬아치일 텐데, 내게 무시당했다는 생각에 기분이 상한 모양이었다.

“어이고, 죄송합니다. 제가 얼마 전에 머리를 다쳐서 자꾸 정신을 놓고 다니네요.”

그냥 적당히 대처한 건데 그제야 현령의 얼굴이 살짝 풀린다.

“으흠, 아니올시다. 극악무도한 마적 놈들을 상대하시느라 노고가 크셨을 텐데. 아, 자그마치 오백이 넘는 마적을 죽였다지요?”

“어…… 오백 명이요?”

“그렇소. 진천검과 산서잠룡. 두 영웅의 무용담을 듣고 얼마나 기뻤는지. 허허.”

저건 어디서 튀어나온 숫자인지 모르겠네.

이번 전투에 참여한 마적들을 통틀어도 삼백 명이 될까 말까고, 그마저도 나와 진무경이 도착했을 때쯤에는 백 명도 채 남지 않았었다.

‘실제로는 풍양이랑 이미 지쳐 있던 마적 칠십 명? 그쯤 되려나?’

뭐, 원래 소문이라는 게 으레 과장되기 마련이지.

“에이, 그건 너무…….”

사실을 얘기해 주려던 찰나, 나와 현령의 대화를 숨죽이고 듣고 있던 사람들 사이로 술렁임이 번졌다.

“오백 명? 산서잠룡과 진천검 둘이서 간 것 아니었나?”

“허어, 그럼 둘이서 오백 명이 넘는 마적단을?”

“세상에, 사람이 어찌 그리 강할 수 있단 말인가!”

띠링.



- 사람들이 당신을 경외 어린 시선으로 바라봅니다.

- 명성이 40 상승합니다!



“너무, 뭐라고 했소?”

나는 어리둥절해하는 현령을 향해 말을 이었다.

“너무 축소됐네요. 실제로는 족히 육백 명 가까이 되었습니다.”

“육백!”

“저랑 둘째 형님이 반반씩 맡았죠.”

“그럼 한 사람당 삼백 명을!”

“음, 정확히는 이백팔십오 명쯤?”

현령은 물론이고 관군까지 입을 딱 벌렸다.

“오오!”

“이백팔십오 명! 심지어 자세해!”

띠링.



- 사람들이 당신을 경외 어린 시선으로 바라봅니다.

- 명성이 40 상승합니다!



혁무진이 이번엔 벌레 보는 것 같은 얼굴로 내게 속삭였다.

“그렇게까지 하고 싶습니까?”

“응.”

“괜히 전공 부풀렸다가 거짓말인 거 들통나면 어쩌시려고요?”

“너랑 월화, 항산검문만 입 다물면 돼. 그러니까 빨리 한마디 거들어.”

“싫습니다. 이 혁무진, 이래 봬도 하늘을 우러러 한 점 부끄러움 없는, 진실 된 삶을 살아온 놈입니다.”

나는 어이가 없어져서 물었다.

“진무경이 내 전각 무너트렸을 때, 있지도 않은 암살자랑 싸운 게 너 아니었냐?”

“…….”

“할 말 없으면 입 닥치고 표정 관리 잘하자. 내 이백팔십…… 몇 명이었지?”

“이백팔십오 명이요.”

“그래, 거기서 삼십 명 정도는 네가 처리한 걸로 해 줄게. 불알 달고 태어났으면 태원진가 수문각주 정도는 해 봐야지. 안 그래?”

“……!”

하늘을 우러러 한 점 부끄럼 없는 진실 된 인생을 살아왔다는 혁무진은, 현란한 혀 드리블로 현령의 마음을 쏙 빼놓았다.

대부분 이, 삼류였던 마적들은 하나같이 일류 고수요, 적토마를 탄 여포가 되었고 풍양은 일검에 산과 바다를 가르는 무적의 고수로 둔갑시켰다.

‘이 자식 입에서 나오는 말은 앞으로 믿고 거른다.’

어찌나 거짓말을 잘하는지 나조차도 저게 진짜인가 헷갈릴 정도다. 당사자인 나도 이런데, 다른 사람들이야 말할 것도 없지.

“……해서. 고원의 절대자 풍양과 극악무도한 적풍단은 항산검문에서 뼈를 묻게 되었지요.”

혁무진의 구라, 아니 이야기가 끝나자마자 곳곳에서 아쉬움 섞인 한숨이 터져 나왔다. 그중에서도 현령의 반응이 가장 열광적이었다.

“허어어어어, 이럴 수가. 어찌 그런 일이…… 무림은 참으로 놀라우면서도 무서운 곳이구려.”

혁무진이 우수에 젖은 눈으로 사람들을 훑어보았다.

“저 같은 무부(武夫)는 두려움이 없습니다. 검을 쥔 후부터 늘 죽음을 벗 삼아 살아가고 있으니까요. 다만 한 가지 소원이 있다면…….”

“있다면?”

“강자의 검에 죽는 것. 그것 말고는 바랄 것이 없습니다.”

“…….”

진짜 이 정도면 지랄이 풍작이다.

나는 혁무진의 뒤통수를 후려치고 싶은 충동을 억누르며 앞으로 나섰다.

명성치는 이미 쪽쪽 빨아 먹어서 더 오르지도 않는 상태. 굳이 배 나온 아저씨랑 계속 얘기를 나눌 이유가 없다.

“말씀 중에 죄송합니다만, 저희가 갈 길이 바빠서요.”

최면에 걸린 것처럼 몽롱한 눈빛으로 혁무진을 바라보던 현령이 그때 퍼뜩 정신을 차렸다.

“아, 미안하오. 내 원래 이러려던 게 아니었는데.”

“그럼 혹시 볼일이라도.”

“진 대협을 뵐 수 있겠소? 소가주님 말이오.”

현령의 시선이 내 등 뒤에 있는 마차를 향한다.

밖에서 보이지는 않지만 안에는 진위경과 진무경, 그리고 위팽이 타고 있었다.

‘술에 떡이 돼서 말이지.’

지난 3일 동안의 주량 대결에서 내게 처참하게 발린 패배자들이다. 하지만 사실대로 말할 수야 있나, 나는 표정 하나 변하지 않고 거짓말을 했다.

“죄송하지만 지금 운기조식 중이시라 뵐 수 없을 것 같습니다. 현령님께서도 아시다시피 상당히 위험한 일이라.”

“아, 그렇구려. 그럼 어쩔 수 없지.”

혀를 찬 현령이 소매에서 돌돌 말린 종이를 꺼내어 내게 건넸다.

“이게 뭡니까?”

“성주(城主)님께서 보내시는 초청장이오. 근래 진 소협의 활약을 들으시고는 아주 큰 감명을 받으셨는지 후기지수 몇 명과 함께 자리를 마련하셨소.”

띠링.



- 퀘스트가 생성되었습니다.
```

## Final English reading copy

```markdown
# Chapter 128

Old Man Jang woke to the sound of a commotion.

*What goddamn bastards are making all that noise?*

He was old enough that his hours of sleep were gradually dwindling, so this was hardly a welcome development.

*I’ll go see what their faces look like.*

Dragging his stiff body out of the thatched cottage, Old Man Jang’s eyes immediately fell on a crowd gathered like clouds.

There were hundreds of them, by his rough estimate. It looked as if everything in the village with legs—human or animal—had gathered in one place.

“What’s all this about?”

It was a small, unremarkable village, so he knew most of the faces.

At Old Man Jang’s muttering, a familiar market merchant greeted him.

“You’re awake, sir.”

“With this kind of racket, how could I stay asleep?”

“Ha-ha, please understand, sir. Everyone’s gathered because they heard an important guest was coming.”

Old Man Jang grunted.

“An important guest? Is the Emperor coming?”

“Oh, there you go again. Is the Emperor your friend?”

“By age, I’d be his father.”

“You’ll get arrested for treason talking like that. Can’t you see the government soldiers over there?”

“Government soldiers?”

Following the merchant’s nod, Old Man Jang spotted dozens of government troops and a man dressed in an official robe—the county magistrate. His eyes narrowed.

“That fellow never showed his face when the mounted bandits were prowling around, but now he’s dressed up in his official robes too? Is this important guest some high-ranking official?”

“Not a high-ranking official, but in Shanxi Province, they’re number one.”

The merchant raised his thumb.

At that very moment, an uproar erupted from the assembled crowd.

“They’re coming!”

“They’re here!”

Old Man Jang turned his head in the direction of everyone’s gaze. When he saw fifty mounted riders charging toward them from the distance, their flags snapping in the wind, he finally understood who the important guests were.

*The Jin Family of Taiyuan.*

Old Man Jang had little interest in the affairs of the world, but he had heard the name of the Jin Family of Taiyuan until his ears rang.

A prestigious family that had maintained its lineage for three hundred years, and the hegemon that held Shanxi Province in its grasp.

As Old Man Jang watched the imposing procession, his brow suddenly furrowed.

*Who was that fellow again? That… what was it? Shanxi, Shanxi… some kind of dragon?*

Age had weakened his memory as well. As Old Man Jang lamented the passing years, one person caught his eye.

“Say, who’s that young man?”

“Ah, that Young Hero?”

There were dozens of martial artists from the Jin Family of Taiyuan alone, all clearly visible. Yet the merchant immediately understood whom he meant.

An awl in a pocket. The young man’s presence was like an awl tucked inside a pouch, bound to stand out wherever he went, so there was nothing strange about it.

“That’s the Sleeping Dragon of Shanxi.”

Shing—

As if he had heard those words, the young man at the head of the procession drew the sword at his waist.

The transparent blade flashed in the sunlight, and a thunderous cheer erupted.

“Waaaaaah!”

“Jin Family of Taiyuan! Sleeping Dragon of Shanxi! Heaven Shaking Sword!”

* * *

“Sleeping Dragon of Shanxi! Jin Taekyung! Sleeping Dragon of Shanxi! Jin Taekyung!”

My epithet and name rang out from every direction. Even though I’d already experienced this several times over the past few days, it still made me feel proud.

*Is this how idols feel?*

It was just like that thing. *Milky-skinned Jin Taekyung. We love you, Jin Taekyung.*

An idol fan club, the kind I’d only ever seen on music variety shows, was right in front of me. Smiling contentedly, I drew the [Unnamed Sword] from my waist.

Shhhng. Flash!

Maybe it was the Ten-Thousand-Year Cold Iron brand, but nothing else came close when it came to visual effects.

“Waaaaaah!”

“Eeeeek! Young Master, take me!”

“Wah! Wah!”

A man for everyone, like something rated for all audiences—men and women, young and old.

That man was me.

Ding.



> **System**
>
> **Fame** rises by 19!
>
> **Fame** rises by 26!
>
> **Fame** rises by 31!
>
> …
>
> …
>
> **Fame** rises significantly!
>
> Due to the increase in **Fame**, the effect of the **Sleeping Dragon of Shanxi** **Title** has been strengthened!

*The Title effect has been strengthened?*

That was an unexpected bonus. I opened my Status Window to check the changes.

Ding.



> **System**
>
> **Status Window**
>
> **Lv. 61 Jin Taekyung**
>
> **Class:** First Rate martial artist
>
> **Fame:** 2,100 (+250)
>
> **Titles:** 4 (Title effects active)
>
> — Returned One (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +15, Fame +200)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+30)  
> **Stamina:** 195 (+30)
>
> **Agility:** 192 (+30)  
> **Intelligence:** 35 (+30)
>
> **Charm:** 35 (+30)  
> **Internal energy:** 45 years
>
> **Toughness:** 155 (+30)
>
> **Remaining points:** 60
>
> — Distribute your remaining points.



The Sleeping Dragon of Shanxi’s Title effect had definitely changed from All stats +10 and Fame +100.

*So my name carries more weight now?*

Titles didn’t simply drop from the heavens.

In my case, rumors about me being some kind of sleeping dragon had gradually spread, and at some point, my Fame rose and I gained the Title Sleeping Dragon of Shanxi.

It seemed that the effect of a Title increased along with one’s Fame.

*My Level has already passed sixty, too.*

The Status Window, which I hadn’t checked in a while, had grown by leaps and bounds. My Fame had shot up, my combat-related stats were approaching 200, and I had a solid forty-five years of internal energy.

*Hehehe. Innkeeper!*

I shuddered with exhilaration, and Hyuk Mujin, who was carrying a flag on my right, looked at me as if I were mentally ill.

“Are you really that happy?”

I deliberately put on a serious face.

“Who said I was happy? People like me, so I was just helping to liven up the mood.”

“……I have a lot to say, but I won’t.”

“Wise choice.”

Walking amid the crowd’s cheers, we pulled on the reins and slowed down.

Dozens of men had poured out into the street and blocked our path.

Among them, a fat man dressed in splendid red robes smiled broadly at me.

“Heh-heh, you’re every bit as dignified and handsome as I’d heard. I’ve long been familiar with the great reputation of the Sleeping Dragon of Shanxi.”

“Ah, yes.”

Confused, I asked,

“But who are you?”

Hyuk Mujin hurriedly whispered,

“He’s the county magistrate. The county magistrate.”

“What’s a county magistrate?”

“What? You don’t even know what a county magistrate is?”

“Is he like a village head?”

“Wow, this is driving me crazy. Just think of him as an official.”

“An official. Then are the people behind him government troops?”

“……Why are you acting like you’ve never seen government troops before?”

“No, I just find it interesting.”

In fact, I really had never seen them before.

I studied the fat man—no, the county magistrate—and his subordinates carefully.

I knew that this world had a government, official offices, and law-enforcement agencies, but this was the first time I’d actually encountered them.

*How could they never show even the tips of their noses?*

Violent crimes happened dozens of times a day in this neighborhood, yet I had never once seen government troops drag away a criminal.

Then again, considering the authorities hadn’t intervened in the Battle of Eight Spring Gorge, where roughly two thousand people had clashed, or in this latest incident involving the Red Wind Band, perhaps that was only natural.

*It’s not as if they’re even beating up the mounted bandits who loiter around.*

What exactly did these bastards do?

I was imagining that, if this were modern times, half the martial artists in the Murim would be locked in solitary confinement for murder when the county magistrate cleared his throat.

“Ahem. Ahem!”

His face flushed red as he coughed awkwardly.

He was an official with a certain position, after all, and seemed offended that I had ignored him.

“Oh, I’m sorry. I injured my head a while ago, so I keep spacing out.”

I’d only offered a reasonable excuse, but the county magistrate’s expression relaxed slightly.

“Ahem, no, no. You must have gone through great hardship dealing with those vicious mounted bandits. Ah, I heard you killed more than five hundred of them?”

“Uh… five hundred?”

“That’s right. I was overjoyed to hear the tales of valor of the two heroes, the Heaven Shaking Sword and the Sleeping Dragon of Shanxi. Ha-ha.”

I had no idea where that number had come from.

Even if you counted every mounted bandit who took part in the battle, there might have been three hundred at most. And by the time Jin Mukyung and I arrived, fewer than a hundred of them had remained.

*In reality, there was Pung Yang and maybe seventy mounted bandits who were already exhausted. Something like that.*

Well, rumors were usually exaggerated.

“Come on, that’s too—”

Just as I was about to explain the truth, murmurs spread through the people who had been listening to my conversation with the county magistrate.

“Five hundred? Didn’t the Sleeping Dragon of Shanxi and the Heaven Shaking Sword go there alone?”

“Good heavens. The two of them defeated a mounted-bandit force of more than five hundred?”

“How can human beings be that strong?”

Ding.



> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!



“Too what did you say?”

I continued speaking to the bewildered county magistrate.

“That’s a serious understatement. In reality, there were nearly six hundred.”

“Six hundred!”

“My second brother and I took half each.”

“Then three hundred each!”

“Hmm. More precisely, about 285?”

The county magistrate—and even the government troops—gaped at me.

“Ooh!”

“Two hundred and eighty-five! And he even knows the exact number!”

Ding.



> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!



This time, Hyuk Mujin whispered to me with an expression usually reserved for looking at a bug.

“Do you really want to take it this far?”

“Yep.”

“What are you going to do if you inflate your achievements for no reason and get caught lying?”

“You, Wolhwa, and the Mount Heng Sword Sect just have to keep your mouths shut. So hurry up and back me up.”

“I refuse. Hyuk Mujin may not look it, but I’ve lived a truthful life without a single shameful moment before the heavens.”

I stared at him in disbelief.

“When Jin Mukyung destroyed my pavilion, weren’t you the one who fought assassins that didn’t even exist?”

“…….”

“If you have nothing to say, shut up and manage your expression. My two hundred and eighty… How many was it?”

“Two hundred and eighty-five.”

“Right. I’ll count about thirty of them as your kills. If you were born with balls, you ought to make Master of the Gatekeeper Pavilion in the Jin Family of Taiyuan at least once in your life. Don’t you think?”

“……!”

Hyuk Mujin, who had lived a truthful life without a single shameful moment before the heavens, used his dazzling tongue to completely win over the county magistrate.

The mounted bandits, most of whom had been Second Rate or Third Rate, became First Rate masters to a man—each a Lü Bu astride Red Hare. Pung Yang became an invincible master who could cleave mountains and seas with a single sword strike.

*From now on, I’m filtering anything that comes out of this bastard’s mouth.*

He was such a skilled liar that even I found myself wondering whether it was true. If even I, the person involved, was confused, there was no hope for anyone else.

“……and that was how Pung Yang, the absolute ruler of Gaoyuan, and the vicious Red Wind Band came to meet their end at the Mount Heng Sword Sect.”

The moment Hyuk Mujin finished his bullshit—his story, I mean—sighs of disappointment rose from all around us. The county magistrate’s reaction was the most enthusiastic of all.

“Whaaaat? How could such a thing happen? The Murim is truly a wondrous yet terrifying place.”

Hyuk Mujin swept his gaze over the crowd with melancholy eyes.

“A martial brute like me has no fear. Ever since I took up the sword, I’ve lived with death as my companion. But if I have one wish…”

“One wish?”

“To die by the sword of someone strong. That is all I could ask for.”

“…….”

At this point, this was a bumper crop of bullshit.

Suppressing the urge to smack Hyuk Mujin in the back of the head, I stepped forward.

I had already milked the Fame for all it was worth, and there was no reason to keep talking to a potbellied middle-aged man.

“Sorry to interrupt, but we’re in a hurry.”

The county magistrate, who had been gazing at Hyuk Mujin with dazed eyes as if hypnotized, suddenly came to his senses.

“Ah, my apologies. I didn’t mean for this to happen.”

“Then do you have some other business?”

“Could I meet Great Hero Jin? I mean, the Lesser Family Head.”

The county magistrate’s gaze shifted toward the carriage behind me.

They couldn’t be seen from outside, but Jin Wikyung, Jin Mukyung, and Wipeng were inside.

*Because they were drunk out of their minds.*

They were the losers who had been utterly crushed by me in our drinking contest over the past three days. But how could I tell him the truth? Without changing my expression, I lied.

“I’m sorry, but he’s currently circulating his qi and won’t be able to see you. As you know, County Magistrate, it’s quite dangerous.”

“Ah, I see. Then it can’t be helped.”

The county magistrate clicked his tongue, then pulled a tightly rolled piece of paper from his sleeve and handed it to me.

“What is this?”

“An invitation from the City Lord. After hearing about your recent exploits, Young Hero Jin, he seems to have been deeply impressed, so he arranged a gathering with several young prodigies.”

Ding.



> **System**
>
> A **Quest** has been created.
```
