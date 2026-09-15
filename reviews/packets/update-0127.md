<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0127.txt",
      "sha256": "6979125ea3378f2d0aadaaca73e31bc2b22cda75829bdfb8c5566fd2abac2110",
      "bytes": 16082
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "75ffb1f921f083821dcd8a6bac168e57fd972b6ac40881a05a0ac348259980af",
      "bytes": 5785
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6e5c2bcc932324f6a2dbe6242adf6ca7feec1419d6e17681ac54c17cc58e4bbd",
      "bytes": 22064
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "5efbf3c1a747b2bb32807b3bf4859ccd7d2629ec055b6418e0076526fec536af",
      "bytes": 5199
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "cdabff0fb722087e196591e3aabd6950ce68d0a81cbcd68fa43c5a87ad060e15",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "a88ff9c6a4f028e67ffecc4f26ca4e13b3e143b52b3e17edaebcf89d6f9e1887",
      "bytes": 8154
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "03024458a4f9638366fe41d289dc2e0cc91c7bbc24a98b573375e741d5bd7cea",
      "bytes": 1356
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "68d4a0e4531e743c98231039971e8e3d8d2168f505a99af095283010aefb3214",
      "bytes": 4604
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "badd58dcf30ec91f3e4cdb1d85fa9dcf4c034b16c7e83f316c248cd44618ccf0",
      "bytes": 18945
    }
  ],
  "estimated_tokens": 22468
}
-->

# Durable State Update — Chapter 127

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 127. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 127. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 127,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 127,
    "continuity_sources": [127],
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
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered after only four days of healing.",
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
    "The Temporary Strength Pill has an unknown maker and unknown Grade, temporarily raises latent power, grants +100 combat stats and fifteen years of internal energy, enables Body-Protecting Qi, and is now confirmed to be stored in Taekyung's Inventory.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers.",
    "Jin Wikyung was told that Pung Yang had died, the Red Wind Band had been annihilated, Taekyung had defeated Pung Yang, and Mukyung had suffered severe but nonfatal injuries.",
    "The Jin Family of Taiyuan displayed a huge Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung revealed his possession of the Temporary Strength Pill to Wikyung, Mukyung, and Wipeng at the chapter's end."
  ],
  "continuity_sources": [
    126
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's origin, exact price, and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Was Jopil truly the nineteenth-generation successor of the Flame Divine Palm, and how did he acquire it?",
    "Who called out to Jin Mukyung and Jin Taekyung from the distance at the chapter's end?"
  ],
  "safe_through": 126,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, and 시진 as shichen.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, and 천하십대권법 as the ten greatest fist techniques in the world.",
    "Render 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, and 태양인 as Taeyangin."
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

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 대주     | **Squad Leader** / **Commander**             |
| 큰형     | **eldest brother**                           |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 126
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; stationed outside Jin Taekyung’s pavilion while Taekyung recovers
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 126
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 126
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 126
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 126
- **Aliases:** Ghost Sword
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

## Korean source

```text
＃127화



물음표가 느낌표로, 느낌표가 황당함과 분노로 바뀌는 데까지는 그리 오랜 시간이 걸리지 않았다.

가장 먼저 정적을 깬 것은 진무경이었다.

“너…….”

벌겋게 달아오른 얼굴, 거친 숨소리. 당장이라도 내 주둥이에 한 방 먹이고 싶은지 주먹이 움찔거린다.

‘음, 제대로 열받았군.’

싸늘하다. 가슴에 비수가 날아와 꽂힌다. 하지만 걱정하지 마라. 내게는 든든한 방패가 있으니까.

“어허, 무경아.”

나직하게 들리는 목소리에 진무경의 얼굴이 와락 일그러졌다.

“형님!”

“태경이도 다 생각이 있었겠지. 안 그러느냐?”

나는 짐짓 눈을 내리깔았다.

“아닙니다. 소제(小弟)의 생각이 짧았습니다.”

“응?”

“호기심에 그만…… 하지만 큰형님의 이야기를 듣고 깨달았습니다. 그것은 결코 갖고 있어서도, 숨겨서도 안 되는 물건이라는 사실을 말입니다.”

생각만 해도 치가 떨린다는 듯이 주먹을 부르르 떠는 연출도 잊지 않았다.

“마교! 그 악독한 놈들의 이름만 들어도 치가 떨립니다!”

이건 진심이다. 기왕 만드는 거 잘 좀 만들지, 광기에 젖은 살인귀가 되는 심각한 결함이 있다니!

“허어.”

나를 바라보는 진위경의 눈빛에 애정이 듬뿍 담겨 있었다.

“나중에 커서 협의지사가 되겠다던 작고 귀여운 꼬마 아이가 생각나는구나. 그때 네 나이가 여섯 살이었다. 기억나느냐?”

당연히 안 나지.

재작년 일도 가물가물한데 이 몸의 원주인이 여섯 살 때 뭘 했는지 알 턱이 있나. 그러나 나는 비장하게 고개를 끄덕였다.

“똑똑히 기억합니다. 제 유일한 꿈이었으니까요.”

협의지사건 경기도지사건, 오늘 이 시간부로 그게 내 여섯 살 때 장래 희망이다.

“허허, 그 어린 녀석이 이렇게 훌륭히 장성하다니.”

흐뭇하게 웃은 진위경이 이번엔 다른 두 사람을 향해 고개를 돌렸다.

“그 자리에 자네도 있었지. 위팽, 기억나는가?”

위팽이 숨도 쉬지 않고 대답했다.

“그건 모르겠고, 그러고서 딱 십 년 후부터 계집질 시작한 건 기억납니다. 커서 뭐가 될 거냐고 물었더니 그때는 천하제일의 풍류남아라고 하던데요.”

“영웅이라면 모름지기 풍류를 알아야지.”

“무공은 쥐뿔도 모르는데 풍류만 알아서 뭐 합니까? 말씀하시는 영웅이 밤의 영웅, 기녀들의 영웅. 뭐 그런 겁니까?”

“조용히 하게. 우리 막내는 어릴 때부터 싹수가 남달랐어.”

“그러니까 그 싹수가…… 어후, 됐습니다. 내가 말을 말아야지.”

벌컥벌컥.

술을 병째로 들이붓는 위팽을 깔끔하게 무시한 진위경의 시선이 다음 주자를 향했다.

“무경아. 이제 막내의 진심을 알았으니 화 풀거라.”

오만상을 쓰고 있던 진무경이 입을 뗐다.

“저 자식 한 대만 때리면 안 됩니까?”

“어허.”

“딱 한 대만. 제발.”

싸늘한 목소리에 내가 재빨리 고개를 숙였다.

“이 못난 아우를 용서하십시오, 둘째 형님.”

“지금까지 반말 찍찍 하던 놈이 형님 같은 소리 하네.”

“예? 제가요?”

“그만해라. 마지막 경고다.”

“아닙니다. 차라리 절 때리십시오. 그렇게라도 형님의 분이 풀리신다면 이 아우, 기꺼이 감내하겠습니다.”

“야, 이 새끼야!”

벌떡 일어난 진무경이 헉, 하는 신음과 함께 도로 주저앉았다. 가슴팍에 동여맨 붕대가 붉게 젖어 드는 걸 보니 상처가 벌어진 모양이다.

“아이고 형님, 괜찮으십니까!”

“이 자식이 또…… 커헉!”

“의원, 의원!”

순식간에 난장판이 되어 버린 술자리.

묵묵히 두 번째 술병을 집어 든 위팽이 중얼거렸다.

“가문 꼴 잘 돌아간다…….”

얼마나 잘 돌아가는지, 무려 산서제일가다.



* * *



결국, 의원이 다녀가고 나서야 분위기가 수습됐다.

나를 찢어 죽일 듯한 진무경의 시선을 외면하고 잠력단을 품에서 꺼냈다.

“바로 이겁니다.”

마치 피를 응축시킨 것처럼 온통 붉은 단환.

진위경과 위팽이 잠력단을 유심히 살폈다.

“위팽, 어떻게 생각하나?”

“보기만 해도 피비린내가 나는군요. 흉악한 물건입니다.”

“정말 마교 쪽에서 만든 걸까?”

“글쎄요. 그렇다면 마기가 느껴져야 하는데…… 저로서는 확신하기 어렵습니다.”

“그렇지? 뭔가 달라.”

두 사람의 표정은 몹시 심각했다. 잠력단을 어디서, 누가 만들었는지 궁금한 건 나도 매한가지라 힌트를 던져 주기로 했다.

“잠력단이라고 하던데요.”

“잠력단?”

“네, 풍양의 입으로 직접 들었어요.”

진무경이 불쑥 끼어들었다.

“풍양이? 도대체 언제?”

“너 기절해 있을 때요.”

“……후욱. 후우욱.”

누가 뭐라고 하든 내가 유일한 목격자고 증인이다. 본전도 못 찾은 진무경이 화를 가라앉히려 호흡을 가다듬을 때, 다른 두 사람은 미간의 골만 깊어지고 있었다.

“잠력단이라, 위팽?”

“저도 처음 들어 봅니다. 이 정도 효력에 마교의 물건이라면 분명 정마대전 때 쓰였을 터인데…….”

“마교가 아닐 수도 있지 않아요?”

두 사람의 시선이 날 향했다.

“마교가 아니다?”

“어찌 그렇게 생각하십니까?”

“처음부터 단정 지을 필요는 없다 이거죠.”

사실 마교가 만든 단환이 아니라면 다시 가져갈 수 있을까 하는 희망 사항에서 나온 말이다.

물론 내 나름대로 달리 떠오른 생각도 있었고.

‘대장로.’

지난번 전쟁에서 표면적으로 드러난 적은 분명 항산검문이었지만 진정한 적은 대장로, 바로 그였다.

이분법적인 추측보다는 제3의 세력이 있을지도 모른다는 가능성을 늘 염두에 둬야 한다는 것이 내 생각이다.

“뭐, 그냥 갑자기 그런 생각이 들었다는 거죠.”

내 말을 모두 들은 두 사람의 표정이 심상치 않다. 그리고 다음 순간, 위팽의 입에서 아주 작은 목소리가 흘러나왔다.

그것은 무의식중에 신음처럼 흘러나온 한 단어였다.

“암천…….”

“위팽.”

진위경의 날카로운 눈빛이 이어지는 말을 틀어막았다.

“아, 죄송합니다. 제가 실언을.”

황급히 얼버무리는 위팽. 하지만 이미 늦었다.

암천이라는 두 글자가 내 뇌리에 깊게 박힌 후였으니까.

‘암천? 그게 뭐지?’

그때, 예상치 못한 일이 일어났다.

띠링.



- [암천]에 관한 미약한 정보를 얻었습니다.

- [잠력단]에 관한 아이템 설명이 변경됩니다.



느닷없는 시스템 알림. 나는 잠력단을 들고 있는 위팽에게 손을 내밀었다.

“제가 잠깐 확인해 봐도 될까요?”

“아, 물론입니다.”

아이템 확인. 마음속으로 중얼거리자 곧장 잠력단에 관한 정보가 떴다.

변경된 정보를 찾는 것은 쉬운 일이었다.



아이템창



[잠력단]

종류 : 영단

등급 : ???

제한 : [절정 무인] 이상

설명 : [암천]이 제조한 단환. 약 한 시진 동안 복용자의 잠재된 힘을 대폭 끌어 올리는 대신, 그에 대한 대가가 뒤따른다. 최악의 경우가 아니고서는 복용하지 말 것.

효과 : 전투 관련 능력치 +100

[공력] +15년

[호신강기] 사용 가능





[알 수 없는 누군가]가 사라지고 [암천]이라는 생소한 단어가 그 자리를 채웠다.

‘문맥으로 봐서 어떤 모종의 단체인 건 확실한데…….’

뭐, 잠력단 같은 물건을 만드는 놈들이니 마교와 비교해도 그 나물에 그 밥일 게 뻔하다.

‘암천.’

누가 지었는지 작명 센스 하나는 끝내준다. 두 글자만으로 자신들이 수상쩍은 놈들이라는 걸 알려 주니까.

이 새끼들 분명히 뒤가 구린 놈들이다. 99퍼센트 확신한다.

‘진위경과 위팽은 뭔가 알고 있는 것 같은데.’

문제는 앞서 두 사람이 보인 반응으로 봤을 때 암천에 관한 정보 노출을 극도로 꺼릴 거라는 사실이다.

‘그래도 한 번 찔러 볼까?’

하지만 정작 내가 입을 열기도 전에, 진무경이 한발 빨리 물었다.

“암천? 그게 뭡니까?”

“그게…….”

진위경의 얼굴 위로 곤란한 빛이 스쳤다.

“미안하구나. 아직은 말해 줄 수 없다.”

동생들을 끔찍이 생각하는 그의 입에서 나온 말이다.

진위경이 이러는데 위팽에게는 물어볼 필요도 없다.

“두 공자님께는 죄송합니다만, 보다 명확해지기 전까지는 알려 드릴 수 없습니다.”

지금까지 보지 못했던 확고한 태도다. 나도, 진무경도 오늘은 이쯤에서 물러나야 한다는 사실을 깨달았다.

다만 그럴수록 암천에 대한 호기심은 더더욱 커져 갔다.

‘우리한테까지 감춰야 할 비밀이라 이거지.’

가문의 직계라는 혈통은 둘째치더라도, 나와 진무경은 태원진가의 핵심 고수다. 진위경의 오른팔이 위팽이라면 각자 왼팔, 한쪽 다리 역할 정도는 하고도 남는다.

‘그럼 가문 내에서도 두 사람만 아는 특급 기밀이라는 건데.’

나도 사람인지라 궁금해지는 건 어쩔 수 없다. 게다가 항산검문 때는 잠잠하던 시스템이 반응했다는 사실도 한몫했다.

‘암천, 잠력단, 진위경과 위팽만 아는 특급 기밀.’

몇 가지 키워드가 머릿속을 휙휙 스쳐 지나간다.

좋아, 결심했다.

‘신경 끄고 살아야지.’

과한 호기심은 명줄을 짧게 만드는 법이다. 항산검문에 우편 배달하러 갔다가 죽을 고비를 넘긴 지 며칠 되지도 않았다.

이름부터가 불길하기 짝이 없는 수수께끼의 단체? 엮였다가는 좋은 꼴 못 볼 게 뻔하다.

“자자, 이 얘기는 그만하고 술이나 한 잔씩들 할까?”

진위경이 억지로 분위기를 환기시킨다.

이미 혼자서 두 병을 아작 낸 위팽도, 부상당한 진무경도 잔을 채우는데 나라고 뺄 수 있나. 진위경이 따라 주는 술을 받아 쭉 들이켰다.

꿀꺽, 꿀꺽.

도수 높기로 악명이 자자한 화주(火酒)가 후끈한 열기와 함께 목을 타고 넘어갔다.

“크으으.”

이야, 이거 장난 아닌데?

도수 높은 거야 알고는 있었지만 직접 마셔 보니 생각 이상이다. 이 정도면 소주, 맥주는 명함도 못 내밀 것 같다.

몸을 부르르 떠는 나와는 달리 나머지 셋은 곧장 빈 술잔을 꽉꽉 채웠다.

“마셔!”

“들이부어!”

“죽을 때까지 달려!”

“…….”

산서성이 화북(華北) 지방에 속하며, 화북 사내들은 하나같이 엄청난 주당이라는 사실을 안 것은 술로 밤을 꼬박 지새우고 난 후였다.



* * *



다음 날 정오. 상쾌한 기분으로 말에 오르는 나를 혁무진이 괴물 보듯 바라봤다.

“속 괜찮으세요?”

“어, 괜찮은데?”

“혹시 어제 혼자 술 안 드신 건 아니죠? 아니면 중간에 주무셨다거나.”

“응, 넷이서 계속 마셨어.”

“……그걸 전부 다요?”

녀석이 입을 딱 벌렸다.

“그게 말이 됩니까? 사람이에요?”

“다 들어가더라.”

“세상에, 도대체 밤새 몇 병을 드신 겁니까?”

단위가 잘못됐다. ‘병’이 아니라 ‘통’이다.

무슨 해적 나오는 영화에서나 보던 거대한 술통을 끊임없이 비우고, 또 비웠다.

“글쎄, 한 스무 통 가까이 마신 것 같은데. 열 통 넘은 후로는 안 세어 봐서 모르겠다.”

“허, 정말 대단하십니다.”

혁무진이 감탄하며 엄지를 추켜세우는데 갑자기 객잔의 문이 열렸다.

그리고 세 마리의 좀비, 아니 세 명의 절정 고수가 모습을 드러낸다.

“흐어어.”

“우욱.”

“허억, 허억.”

창백한 안색, 바짝 마른 입술과 퀭한 눈동자.

한 명의 예외도 없이 발을 질질 끌며 마차로 쏙 들어가는 모습에 호위대의 무인들이 눈을 휘둥그레 떴다.

“갑자기 왜 마차를…….”

“상태가 많이 안 좋으신 것 같은데?”

“그럴 리가. 자네들 우리 대주님이랑 술 안 마셔 봤어? 주신(酒神) 위팽. 몰라?”

“대주님 별호는 귀검 아니었습니까?”

“모르긴 몰라도 주량으로 따지면 무신(武神)도 이길걸. 그냥 지금까지의 피로가 쌓여서 저러시는 거겠지.”

무인들이 쑥덕거리던 그때, 마차 문이 벌컥 열리더니 한 사람이 후다닥 뛰쳐나와 허리를 숙였다.

“꺼억, 끄우웨에에엑!”

촤르르르륵.

희멀건 액체만 한참 쏟아 내고 비틀비틀 마차로 복귀하는 위팽의 뒷모습에 한창 떠들던 무인이 얼떨떨한 목소리로 중얼거렸다.

“……이럴 리가 없는데.”

“이럴 리가 없긴. 저건 누가 봐도 숙취지. 잠도 안 주무시고 그렇게 마셔 댔으니 저러실 만도 해.”

“그럼 삼공자님은 왜 저렇게 멀쩡하신데?”

호위대의 시선이 내게로 쏠렸다. 전신에서 섬뜩할 정도로 풍기는 술 냄새. 하지만 그와는 반대로 상쾌하기 짝이 없는 얼굴과 편안한 호흡.

“설마?”

“삼공자님이 대주님을 이겼다고? 그 주신을?”

술렁이는 장내.

이제 혁무진은 감탄을 넘어 존경의 눈빛을 보내고 있었다.

“아아, 역시! 허구한 날 기녀들 끼고 술 마시던 조장님 수준!”

“…….”

“조장님이 삼 년만 더 술을 마셨으면 본가 기둥뿌리가 뽑혔을 거라는 총관님 말씀이 생각납니다. 이래서 항상 공금을 훔칠 수밖에 없었던 거였군요!”

“……야, 인마.”

단둘이 있는 것도 아니고, 그딴 식으로 말하면 내 이미지가 뭐가 되냐.

안 그래도 아까부터 사방에서 우수수 꽂혀 드는 시선에 얼굴이 따가울 지경이다.

“커흠. 커흐흠!”

헛기침하며 슬쩍 주위를 둘러봤는데 이게 웬걸. 시커먼 사내놈들 눈동자가 밤하늘 샛별보다 반짝거리는 중이다.

“진정한 주신, 주신이다.”

“태원 홍등가에서는 유명하시지. 야왕이라고 못 들어 봤나?”

“야왕? 별호만 들어도 알겠다. 원래 술 잘 드시는 걸로 정평이 나 있으셨구먼.”

“그게 아니라…… 그거. 그거.”

“허억. 정말인가?”

“나야 모르지. 본 적이 없으니까.”

“알고 보니 진정한 사내셨구먼.”

띠링.



- 이 자리에 모인 이들이 당신의 주량과 위용에 감탄합니다!

- 명성이 20 상승합니다!

- 명성이 22 상승합니다!

- 명성이 25 상승합니다!

- 특정 소문이 퍼질 시, 관련된 칭호를 얻을 수 있습니다.



“…….”

아니 시발, 명성 쭉쭉 오르는 거 뭔데.

그리고 관련된 칭호라니. 괜찮아, 넣어 둬. 제발 산서잠룡으로 만족하게 해 줘.

‘그만해. 이 미친놈들아…….’

이유 모를 수치심과 함께 고개를 돌린 나는, 내 특정 부위를 뚫어져라 바라보는 혁무진과 마주할 수 있었다.

“……뭐 하냐, 지금?”

“아, 잠깐 눈대중으로 재 보고 있었습니다.”

너무 당당하게 대답해서 당황스러울 정도다. 혁무진이 해맑게 웃으며 팔뚝을 내밀었다.

“이야, 역시 대단하십니다. 헤헤.”

나는 팔뚝에 대한 답례로 주먹을 내밀었다.

뻑!
```

## Final English reading copy

```markdown
# Chapter 127

It didn’t take long for the question marks to turn into exclamation points, and the exclamation points to turn into bewilderment and rage.

Jin Mukyung was the first to break the silence.

“You…”

His face was flushed red, and his breathing was rough. His fist twitched as if he wanted to plant one right in my mouth.

*Well, he’s really pissed.*

It was chilling. A dagger had flown straight into my chest.

But don’t worry. I had a sturdy shield.

“Now, now, Mukyung.”

At the quiet voice, Jin Mukyung’s face twisted violently.

“Eldest brother!”

“Taekyung must have had his reasons. Isn’t that right?”

I deliberately lowered my eyes.

“No, eldest brother. I was short-sighted.”

“Hm?”

“I let my curiosity get the better of me… But after hearing what Eldest Brother said, I realized something. It’s an object that should never be kept—or hidden.”

I didn’t forget to make a show of trembling my fist, as if merely thinking about it made my teeth chatter with rage.

“The Demonic Cult! Just hearing the name of those vile bastards makes me tremble with fury!”

This part was sincere. If you’re going to make something, make it properly. Why did it have such a serious defect that it turned people into deranged murderers?

“Good heavens.”

Jin Wikyung looked at me with eyes full of affection.

“I remember a small, adorable little boy who said he would grow up to become a chivalrous hero. You were six years old then. Do you remember?”

Of course I didn’t.

The events of the year before last were already hazy. How was I supposed to know what the original owner of this body had done at age six?

Still, I nodded solemnly.

“I remember it clearly. It was my only dream.”

Whether it was a chivalrous hero or the governor of Gyeonggi Province, as of this moment, that was my career aspiration at age six.

“Ha-ha. To think that little boy would grow up so splendidly.”

After laughing with satisfaction, Jin Wikyung turned toward the other two people.

“You were there too, Wipeng. Do you remember?”

Wipeng answered without even taking a breath.

“I don’t remember that, but I do remember him starting to womanize exactly ten years later. When I asked what he wanted to be when he grew up, he said he’d become the greatest ladies’ man under heaven.”

“A hero ought to know how to enjoy romance.”

“He doesn’t know squat about martial arts, so what good is knowing about romance? Is the hero you’re talking about a hero of the night, a hero to courtesans, or something?”

“Be quiet. Our youngest showed unusual promise from an early age.”

“So that promise… Ah, never mind. I should just stop talking.”

Glug, glug.

Jin Wikyung completely ignored Wipeng, who was pouring liquor straight from the bottle, and turned his attention to the next man in line.

“Mukyung. Now that you understand your little brother’s sincerity, let go of your anger.”

Jin Mukyung, who had been making a face like he’d swallowed something foul, finally spoke.

“Can’t I hit that bastard just once?”

“Now, now.”

“Just once. Please.”

At the icy voice, I quickly lowered my head.

“Please forgive this foolish little brother, Second Brother.”

“The bastard who’s been speaking casually to me this whole time is suddenly calling me ‘brother.’”

“Pardon? I am?”

“That’s enough. This is your final warning.”

“No. Hit me instead. If that would ease your anger, this little brother will gladly endure it.”

“You little shit!”

Jin Mukyung shot to his feet, then sank back down with a gasp. The bandages tied around his chest were turning red. It seemed his wound had reopened.

“Oh, no! Second Brother, are you all right?”

“This bastard, again… Guh!”

“Doctor! Doctor!”

The drinking party became a complete disaster in an instant.

Wipeng quietly picked up his second bottle and muttered,

“This family is really something…”

And how something it was—the foremost family in Shanxi.

* * *

The atmosphere finally settled down after the physician had come and gone.

I ignored Jin Mukyung’s murderous glare and took the Temporary Strength Pill from inside my robes.

“This is it.”

The pill was entirely red, as if blood had been condensed into a single sphere.

Jin Wikyung and Wipeng examined it closely.

“Wipeng, what do you think?”

“Just looking at it makes me smell blood. It’s a vicious object.”

“Could it really have been made by the Demonic Cult?”

“I couldn’t say. If it were, we should be able to sense demonic qi… but I can’t be certain.”

“Right? There’s something different about it.”

Both of them looked extremely serious. I was just as curious about where the Temporary Strength Pill had come from and who had made it, so I decided to give them a hint.

“They called it a Temporary Strength Pill.”

“A Temporary Strength Pill?”

“Yes. I heard it directly from Pung Yang.”

Jin Mukyung suddenly cut in.

“Pung Yang? When did you hear that?”

“While you were unconscious.”

“…Hoo. Hoo…”

I was the only eyewitness and witness, no matter what anyone said. As Jin Mukyung, who had gotten nowhere with his interruption, steadied his breathing to calm himself, the furrows between the other two men’s brows only deepened.

“A Temporary Strength Pill, Wipeng?”

“I’ve never heard of it either. If an object with this level of efficacy belonged to the Demonic Cult, it must have been used during the Great Faction War…”

“Could it not be the Demonic Cult?”

Their gazes turned toward me.

“Not the Demonic Cult?”

“What makes you think that?”

“I’m saying there’s no need to decide that from the start.”

In truth, I had said it out of hope that I might be able to take the pill back if it hadn’t been made by the Demonic Cult.

Of course, I had another thought as well.

*The Head Elder.*

The Mount Heng Sword Sect had certainly been the enemy that appeared on the surface during the last battle, but the true enemy had been the Head Elder himself.

Rather than making a simple either-or assumption, I believed we always had to keep open the possibility that there might be a third faction involved.

“Well, it just suddenly occurred to me.”

After hearing me out, the other two men’s expressions grew strange. Then, in the next moment, a very quiet voice escaped Wipeng’s lips.

It was a single word that slipped out unconsciously, like a groan.

“Dark Heaven…”

“Wipeng.”

Jin Wikyung’s sharp gaze cut off whatever he had been about to say.

“Ah, I apologize. I misspoke.”

Wipeng hurriedly tried to cover it up.

But it was already too late.

The two words *Dark Heaven* had been deeply etched into my mind.

*Dark Heaven? What is that?*

Then something unexpected happened.

> **System**
>
> You have obtained a small amount of information about **Dark Heaven**.
>
> The item description for the **Temporary Strength Pill** will be updated.

It was a completely sudden System notification. I held out my hand toward Wipeng, who was holding the Temporary Strength Pill.

“May I take a quick look?”

“Of course.”

*Item check.*

As soon as I muttered the words in my mind, information about the Temporary Strength Pill appeared.

Finding the changed information was easy.

> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by **Dark Heaven**. For approximately one shichen, it dramatically raises the user’s latent power, but a price follows. Do not take it except in the worst circumstances.  
> **Effects:** Combat-related stats +100  
> Internal energy +15 years  
> Body-Protecting Qi available

The phrase *Someone Unknown* had disappeared, replaced by the unfamiliar term *Dark Heaven*.

*Judging by the context, it’s definitely some kind of organization…*

Well, anyone capable of making something like the Temporary Strength Pill was bound to be no better than the Demonic Cult. Same rotten lot, different name.

*Dark Heaven.*

Whoever came up with the name had incredible instincts. Two words were enough to tell everyone they were suspicious bastards.

*These guys definitely have something rotten going on behind the scenes. Ninety-nine percent sure.*

*Jin Wikyung and Wipeng seem to know something.*

The problem was that, judging by their reactions, they were extremely reluctant to reveal anything about Dark Heaven.

*Should I poke at them once?*

But before I could open my mouth, Jin Mukyung beat me to it.

“Dark Heaven? What is that?”

“Well…”

A troubled look crossed Jin Wikyung’s face.

“I’m sorry. I can’t tell you yet.”

Those words came from a man who cared deeply for his younger brothers.

If Jin Wikyung was unwilling to speak, there was no need to ask Wipeng.

“I apologize, Young Masters, but I cannot tell you until the matter becomes clearer.”

His attitude was firmer than anything I had seen from him before. Both Jin Mukyung and I realized that we had to withdraw for today.

But the more they tried to hide it, the more curious I became about Dark Heaven.

*So it’s a secret they have to keep hidden even from us.*

Even putting aside the fact that Mukyung and I were direct descendants of the family, we were core masters of the Jin Family of Taiyuan. If Wipeng was Jin Wikyung’s right arm, the two of us were each more than qualified to serve as his left arm or one of his legs.

*Then it must be a top-secret matter known only to those two, even within the family.*

I was only human, so I couldn’t help being curious. The fact that the System had reacted this time, despite remaining silent during the Mount Heng Sword Sect incident, also played a part.

*Dark Heaven. The Temporary Strength Pill. A top-secret matter known only to Jin Wikyung and Wipeng.*

Several keywords flashed through my mind.

All right. I’d made up my mind.

*I’ll ignore it and go on living.*

Excessive curiosity had a way of shortening one’s life. It had only been a few days since I’d gone to deliver the mail to the Mount Heng Sword Sect and nearly died.

A mysterious organization whose very name was ominous? If I got involved with them, it was obvious things wouldn’t end well.

“Well, let’s stop talking about this and have another drink.”

Jin Wikyung forced the mood back to normal.

Wipeng, who had already demolished two bottles by himself, was filling his glass, and so was the injured Mukyung. How could I be the only one to sit out? I accepted the liquor Jin Wikyung poured and downed it in one gulp.

Gulp, gulp.

The notorious fire liquor burned its way down my throat with a fierce heat.

“Guhhh.”

Wow. This was no joke.

I knew it was strong, but drinking it myself, it was far more potent than I’d expected. At this strength, soju and beer couldn’t even hold a candle to it.

Unlike me, who shuddered from head to toe, the other three immediately filled their empty glasses to the brim.

“Drink!”

“Down it!”

“Let’s keep going until we drop!”

“….”

I didn’t learn that Shanxi Province belonged to North China, or that every man from North China was an incredible drinker, until after we spent the entire night drinking.

* * *

The next day at noon, Hyuk Mujin stared at me as if I were a monster when I mounted my horse in a perfectly refreshed mood.

“Is your stomach all right?”

“Yeah. Why wouldn’t it be?”

“Don’t tell me you were the only one who didn’t drink yesterday. Or did you fall asleep halfway through?”

“No. The four of us kept drinking.”

“…All of it?”

His mouth fell open.

“Is that even possible? Are you human?”

“It all fit.”

“My goodness. How many bottles did you drink through the night?”

He had the wrong unit.

It wasn’t bottles. It was barrels.

We kept emptying massive casks of liquor—the kind I’d only ever seen in pirate movies—and then emptying more.

“I think it was close to twenty barrels. I stopped counting after ten, so I’m not sure.”

“Wow. That’s incredible.”

Hyuk Mujin raised his thumb in admiration when the inn door suddenly opened.

And three zombies—or rather, three Peak masters—appeared.

“Uuugh.”

“Urk.”

“Huff, huff.”

Their faces were pale, their lips parched, and their eyes sunken.

Without a single exception, they dragged their feet and climbed straight into the carriage. The martial artists of the escort force stared at them with their eyes wide.

“Why are they suddenly getting into the carriage…?”

“They look really unwell.”

“That can’t be. Haven’t you ever drunk with our Commander? Wipeng, the God of Drinking? You don’t know?”

“Wasn’t the Commander’s epithet Ghost Sword?”

“Whatever else you might say, when it comes to drinking, he could probably beat even the Martial God. They’re probably just like this because all the fatigue they’ve accumulated finally caught up with them.”

As the martial artists whispered among themselves, the carriage door suddenly flew open, and one person hurriedly dashed out and bent over.

“Urrp, buuurrgh!”

Splaaarsh.

After pouring out a pale liquid for quite some time, Wipeng staggered back into the carriage. One of the martial artists who had been talking animatedly muttered in a dazed voice,

“…This can’t be.”

“It absolutely can. Anyone can see that’s a hangover. They drank all night without sleeping. Of course they’d end up like that.”

“Then why is the Third Young Master so perfectly fine?”

The escort force’s gazes all turned toward me.

The smell of liquor radiating from my entire body was strong enough to send chills down the spine. But in complete contrast, my face looked unbelievably refreshed, and my breathing was calm.

“No way…”

“The Third Young Master beat the Commander? That God of Drinking?”

The courtyard buzzed with excitement.

Hyuk Mujin’s look of admiration had gone beyond admiration and become outright reverence.

“Ah, I knew it! That’s our Captain—the man who used to drink with courtesans every damn day!”

“….”

“I remember what the Chief Steward said. If Captain had kept drinking for three more years, he would have uprooted the family’s entire foundation. So this is why you always had to steal from the family coffers!”

“…Hey, you punk.”

It wasn’t as if we were alone. If he talked like that, what would happen to my image?

As if the stares pouring in from every direction hadn’t already made my face feel hot enough.

“Ahem. Ahem!”

I cleared my throat and glanced around. And what do you know? The eyes of all those rough-looking men were sparkling brighter than stars in the night sky.

“A true God of Drinking. He really is.”

“He’s famous in Taiyuan’s red-light district. Haven’t you heard of the Night King?”

“The Night King? I can tell just from the epithet. So he was already renowned for his drinking.”

“No, not that… The other thing. That.”

“Gasp. Is it true?”

“How would I know? I’ve never seen it.”

“Turns out he really is a man among men.”

> **System**
>
> Everyone gathered here is impressed by your drinking capacity and imposing presence!
>
> **Fame** rises by 20!
>
> **Fame** rises by 22!
>
> **Fame** rises by 25!
>
> If a particular rumor spreads, you may obtain a related **Title**.

“….”

What the fuck was with my Fame shooting up like that?

And what did it mean, a related Title? No, it was fine. Put that away. Please, just let me be satisfied with the Sleeping Dragon of Shanxi.

*Stop it, you lunatics…*

With a mysterious sense of shame, I turned my head—and came face-to-face with Hyuk Mujin, who was staring intently at a certain part of me.

“…What are you doing?”

“Oh, I was just taking a rough measurement with my eyes.”

His answer was so straightforward that I was almost thrown off. Hyuk Mujin cheerfully extended his forearm.

“Wow. As expected, you’re amazing. Hehe.”

In return for the forearm, I offered him my fist.

Thwack!
```
